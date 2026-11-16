"""Quản lý trình duyệt Playwright tối ưu hóa cho hệ điều hành Windows 10/11.

Sử dụng Google Chrome (hoặc Chromium tích hợp) với cấu hình ẩn dấu vết tự động hóa
(`--disable-blink-features=AutomationControlled`) phục vụ thu thập dữ liệu và Live Demo.
"""

from contextlib import contextmanager

from playwright.sync_api import sync_playwright

# User-Agent chuẩn trên hệ điều hành Windows 10/11 (64-bit)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)


@contextmanager
def browser(headless: bool = False):
    """Khởi chạy trình duyệt Chrome trên Windows và trả về BrowserContext đã cấu hình."""
    with sync_playwright() as p:
        launch_args = [
            "--disable-blink-features=AutomationControlled",
            "--no-default-browser-check",
            "--disable-infobars",
        ]
        try:
            b = p.chromium.launch(
                channel="chrome",
                headless=headless,
                args=launch_args,
            )
        except Exception:
            # Dự phòng sử dụng Chromium đi kèm Playwright nếu máy chưa cài Chrome ở đường dẫn mặc định
            b = p.chromium.launch(
                headless=headless,
                args=launch_args,
            )

        ctx = b.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1366, "height": 768},
            locale="vi-VN",
        )
        # Ẩn thuộc tính navigator.webdriver để tránh bị chặn bởi bộ lọc bot cơ bản
        ctx.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        try:
            yield ctx
        finally:
            try:
                ctx.close()
            except Exception:
                pass
            try:
                b.close()
            except Exception:
                pass

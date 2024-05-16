import os

import logger
from services.sales_report_service import SalesReportService
from services.order_service import OrderService
from utils.console_manager import ConsoleManager
from utils.interactive_menu_handler import InteractiveMenuHandler
from utils.sales_report_pdf_generator import SalesReportPdfGenerator


class Sales:
    @staticmethod
    def display_interaction_menu():
        options = [
            ("Wyświetl sprzedaż", Sales.display_sales_reports),
            ("Generuj raport podsumowania sprzedaży za okres", Sales.generate_sales_reports),
            ("Powrót", lambda: "back")
        ]
        menu_handler = InteractiveMenuHandler(options)
        menu_handler.run()

    @staticmethod
    def display_sales_reports():
        ConsoleManager.display_message("Wyświetlanie raportów sprzedaży")

        options = [
            ("Wyświetl wszystkie raporty", Sales.__get_all_sales_reports),
            ("Wyświetl raport po identyfikatorze", Sales.__get_sales_report_by_id),
            ("Wyświetl raport po dacie utworzenia", Sales.__get_sales_report_by_creation_date),
            ("Wyświetl raport po zakresie dat", Sales.__get_sales_report_by_date_range),
            ("Powrót", lambda: "back")
        ]
        menu_handler = InteractiveMenuHandler(options)
        menu_handler.run()

    @staticmethod
    def generate_sales_reports():
        ConsoleManager.display_message("Generowanie raportu sprzedaży")
        date_start = ConsoleManager.get_input("Wpisz datę początkową dla zamówień (format: YYYY-MM-DD): ")
        date_end = ConsoleManager.get_input("Wpisz datę końcową dla zamówień (format: YYYY-MM-DD):")

        orders = OrderService.get_order_by_date_range(date_start, date_end, 4)

        if not os.path.exists("reports"):
            os.makedirs("reports")

        try:
            report_file_path = SalesReportPdfGenerator.generate_pdf_with_pdfkit(orders, date_start, date_end)
            ConsoleManager.display_message(f"Raport sprzedaży został wygenerowany w pliku: {report_file_path}")
        except Exception as e:
            ConsoleManager.display_message(f"Nie udało się wygenerować raportu sprzedaży: {e}")
            logger.error(f"Failed to generate sales report: {e}")

    @staticmethod
    def __get_all_sales_reports():
        reports = SalesReportService.get_all_sales_reports()

        if not reports:
            ConsoleManager.display_message("Brak raportów do wyświetlenia")
            return

        for report in reports:
            ConsoleManager.display_message(str(report))

    @staticmethod
    def __get_sales_report_by_id():
        ConsoleManager.display_message("Wyświetlanie raportu po identyfikatorze")
        report_id = ConsoleManager.get_input("Podaj identyfikator raportu: ")
        report = SalesReportService.get_sales_report_by_id(report_id)

        if not report:
            ConsoleManager.display_message("Brak raportu do wyświetlenia")
            return

        ConsoleManager.display_message(str(report))

    @staticmethod
    def __get_sales_report_by_creation_date():
        ConsoleManager.display_message("Wyświetlanie raportu po dacie utworzenia")
        date = ConsoleManager.get_input("Podaj datę utworzenia raportu w formatcie YYYY-MM-DD: ")
        reports = SalesReportService.get_sales_report_by_creation_date(date)

        if not reports:
            ConsoleManager.display_message("Brak raportów do wyświetlenia")
            return

        for report in reports:
            ConsoleManager.display_message(str(report))

    @staticmethod
    def __get_sales_report_by_date_range():
        ConsoleManager.display_message("Wyświetlanie raportu po zakresie dat")
        date_start = ConsoleManager.get_input("Podaj datę początkową zakresu w formacie YYYY-MM-DD: ")
        date_end = ConsoleManager.get_input("Podaj datę końcową zakresu w formacie YYYY-MM-DD: ")
        reports = SalesReportService.get_sales_report_by_date_range(date_start, date_end)

        if not reports:
            ConsoleManager.display_message("Brak raportów do wyświetlenia")
            return

        for report in reports:
            ConsoleManager.display_message(str(report))

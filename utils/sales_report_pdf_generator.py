import os
from datetime import datetime
import pdfkit
from database.database import SessionLocal
from models.dish import Dish
from models.drink import Drink
from services.order_dish_service import OrderDishService
from services.order_drink_service import OrderDrinkService


class SalesReportPdfGenerator:
    @staticmethod
    def generate_pdf_with_pdfkit(orders, date_start: str, date_end: str):
        session = SessionLocal()

        try:
            template_path = os.path.join(os.getcwd(), 'templates/sales_report_template.html')
            with open(template_path, 'r') as file:
                html_template = file.read()

            orders_html = ""
            total_count = len(orders)
            total_value = 0.0

            for order in orders:
                # Assuming these services return a list of Dish/Drink IDs
                dish_ids = [od.dish_id for od in OrderDishService.get_order_dishes(order.id)]
                drink_ids = [od.drink_id for od in OrderDrinkService.get_order_drinks(order.id)]

                dish_details = session.query(Dish).filter(Dish.id.in_(dish_ids)).all()
                drink_details = session.query(Drink).filter(Drink.id.in_(drink_ids)).all()

                products = ""
                total_order_value = order.total
                total_value += float(total_order_value)  # Convert Decimal to float

                for dish in dish_details:
                    products += f"{dish.name} ({dish.price:.2f} PLN), "
                for drink in drink_details:
                    products += f"{drink.name} ({drink.price:.2f} PLN), "

                orders_html += f"""
                    <tr>
                        <td>{order.id}</td>
                        <td>{order.customer}</td>
                        <td>{products.rstrip(', ')}</td>
                        <td>{total_order_value:.2f} PLN</td>
                    </tr>
                """

            html = html_template.replace('<!-- Orders will be inserted here -->', orders_html)
            html = html.replace('{{ date_range }}', f"{date_start} to {date_end}")
            html = html.replace('{{ total_count }}', str(total_count))
            html = html.replace('{{ orders_value }}', f"{total_value:.2f} PLN")

            # Save the report with a unique timestamp in the filename
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            output_path = os.path.join(os.getcwd(), f"reports/{timestamp}_sales_report.pdf")
            pdfkit.from_string(html, output_path, options={'page-size': 'A4'})

            return output_path
        finally:
            session.close()

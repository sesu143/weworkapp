import flet as ft
from datetime import datetime

ADMIN_STORE = {
    "orders": [
        {"id": "ORD-1001", "type": "Project Order", "title": "AI Face Recognition System", "name": "Rahul V.", "phone": "9876543210", "email": "rahul@gmail.com", "date": "2026-10-30", "status": "Pending"},
    ],
    "projects": [
        {"id": "P-01", "category": "B.Tech / Diploma CSE", "title": "AI Face Recognition Attendance System", "price": "₹5,000"},
        {"id": "P-02", "category": "B.Tech / Diploma CSE", "title": "Smart IoT Home Automation using ESP32 & Python", "price": "₹4,500"},
        {"id": "P-03", "category": "B.Tech / Diploma CSE", "title": "Secure Encrypted Chat Application with Onion Routing", "price": "₹4,000"},
        {"id": "P-04", "category": "B.Tech / Diploma CSE", "title": "E-Commerce Web Application with Django & FastAPI", "price": "₹5,500"},
        {"id": "P-05", "category": "B.Tech / Diploma CSE", "title": "Sericulture Farming Information & Monitoring Portal", "price": "₹4,500"},
        {"id": "P-06", "category": "B.Tech / Diploma CSE", "title": "Autonomous Line Following & Obstacle Avoiding Robot", "price": "₹4,200"},
        {"id": "P-07", "category": "B.Tech / Diploma CSE", "title": "Plant Disease Detection using Deep Learning & CNN", "price": "₹5,000"},
        {"id": "P-08", "category": "B.Tech / Diploma CSE", "title": "Smart Traffic Signal Control System using Image Processing", "price": "₹4,800"},
        {"id": "P-09", "category": "B.Tech / Diploma CSE", "title": "Weather Forecasting and Air Quality Monitoring System", "price": "₹4,300"},
        {"id": "P-10", "category": "B.Tech / Diploma CSE", "title": "Hospital Management System with Patient Record Encryption", "price": "₹5,200"},
        {"id": "P-11", "category": "B.Tech / Diploma CSE", "title": "Fake News Detection System using Natural Language Processing", "price": "₹4,600"},
        {"id": "P-12", "category": "B.Tech / Diploma CSE", "title": "Automated Student Result Management & Analytics Portal", "price": "₹4,000"},
        {"id": "P-13", "category": "B.Tech / Diploma CSE", "title": "Real-time Vehicle Tracking System using GPS and IoT", "price": "₹5,000"},
        {"id": "P-14", "category": "B.Tech / Diploma CSE", "title": "Online Blood Bank Management and Donor Finder System", "price": "₹4,200"},
        {"id": "P-15", "category": "B.Tech / Diploma CSE", "title": "Smart Parking Slot Booking System using IoT and Python", "price": "₹4,500"},
        {"id": "P-16", "category": "B.Tech / Diploma CSE", "title": "Cybercrime Reporting and Incident Management Portal", "price": "₹4,700"},
        {"id": "P-17", "category": "B.Tech / Diploma CSE", "title": "Automated Library Management System with Barcode Scanner", "price": "₹4,000"},
        {"id": "P-18", "category": "B.Tech / Diploma CSE", "title": "Stock Price Prediction Web App using Machine Learning", "price": "₹4,900"},
        {"id": "P-19", "category": "B.Tech / Diploma CSE", "title": "Women Safety Smart Band with Emergency GPS Alert", "price": "₹5,100"},
        {"id": "P-20", "category": "B.Tech / Diploma CSE", "title": "Blockchain-Based Electronic Voting System Prototype", "price": "₹5,500"},
    ],
    "services": [
        {"name": "Static & Dynamic Web Development", "desc": "Custom responsive websites with clean code and modern UI/UX."},
        {"name": "E-Commerce Solutions", "desc": "Online ordering platforms for local shops, hotels, and businesses."},
        {"name": "Final Year Academic Projects", "desc": "Complete source code, documentation, reports, and PPT support."}
    ],
    "reviews": [
        {"name": "Karthik R.", "rating": "★★★★★", "comment": "Got my final year CSE project done here. Exceptional support and clean code!"},
        {"name": "Priya M.", "rating": "★★★★★", "comment": "Super fast e-commerce website setup for our local store. Highly recommended!"}
    ]
}

def main(page: ft.Page):
    page.title = "We Work Solutions"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B0F19"
    
    PRIMARY_COLOR = "#00F2FE"
    CARD_BG = "#131C2E"
    TEXT_WHITE = "#FFFFFF"
    TEXT_MUTED = "#CBD5E1"

    content_area = ft.Column([], spacing=15, expand=True)

    def nav_to(route):
        route_indices = {"home": 0, "projects": 1, "order": 2, "shops": 3, "reviews": 4}
        if route in route_indices:
            nav_bar.selected_index = route_indices[route]

        content_area.controls.clear()
        if route == "home":
            load_home_view()
        elif route == "projects":
            load_projects_view()
        elif route == "order":
            load_order_view()
        elif route == "shops":
            load_shops_view()
        elif route == "reviews":
            load_reviews_view()
        elif route == "admin":
            load_admin_view()
        page.update()

    nav_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor="#0F172A",
        indicator_color="#1E293B",
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SCHOOL, label="Projects"),
            ft.NavigationBarDestination(icon=ft.Icons.ADD_SHOPPING_CART, label="Order Project"),
            ft.NavigationBarDestination(icon=ft.Icons.STORE, label="Shops"),
            ft.NavigationBarDestination(icon=ft.Icons.STAR, label="Reviews"),
        ],
        on_change=lambda e: nav_to(["home", "projects", "order", "shops", "reviews"][e.control.selected_index])
    )

    def prompt_admin_password(e):
        pwd_input = ft.TextField(
            label="Enter Admin Password", 
            password=True, 
            can_reveal_password=True, 
            border_color=PRIMARY_COLOR,
            text_size=13,
            color=TEXT_WHITE
        )
        
        def verify_password(e):
            if pwd_input.value == "1234":
                page.dialog.open = False
                page.update()
                nav_to("admin")
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Incorrect Password! (Default: 1234)"), bgcolor=ft.Colors.RED_900)
                page.snack_bar.open = True
                page.update()

        dlg = ft.AlertDialog(
            title=ft.Text("🔒 Admin Authentication", color=TEXT_WHITE, size=16, weight=ft.FontWeight.BOLD),
            content=ft.Column([
                ft.Text("Please enter the admin password to view stored orders.", size=12, color=TEXT_MUTED),
                pwd_input
            ], tight=True, spacing=10),
            actions=[
                ft.ElevatedButton("Login", bgcolor=PRIMARY_COLOR, color="#000", on_click=verify_password),
                ft.TextButton("Cancel", on_click=lambda e: setattr(page.dialog, 'open', False) or page.update())
            ],
            bgcolor="#131C2E"
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    app_bar = ft.Container(
        content=ft.Row(
            [
                ft.Row([
                    ft.Image(src="logo.png", width=30, height=30, fit="contain"),
                    ft.Text("WE WORK SOLUTIONS", weight=ft.FontWeight.BOLD, size=14, color=TEXT_WHITE)
                ], spacing=8),
                ft.Row([
                    ft.IconButton(
                        ft.Icons.ADMIN_PANEL_SETTINGS, 
                        icon_color=PRIMARY_COLOR, 
                        tooltip="Admin Panel (Secured)", 
                        on_click=prompt_admin_password
                    ),
                ])
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
        bgcolor="#0F172A",
        border=ft.border.only(bottom=ft.border.BorderSide(1, "#1E293B"))
    )

    def send_whatsapp_order(item_name, name, phone, email):
        msg = f"*New Order / Inquiry*%0A*Project:* {item_name}%0A*Name:* {name}%0A*Mobile:* {phone}%0A*Email:* {email}"
        whatsapp_url = f"https://wa.me/917995148054?text={msg}"
        page.launch_url(whatsapp_url)

    def load_home_view():
        hero = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Text("🚀 INNOVATIVE IT & ACADEMIC SOLUTIONS", color=PRIMARY_COLOR, size=11, weight=ft.FontWeight.BOLD),
                    padding=ft.padding.symmetric(horizontal=10, vertical=4),
                    bgcolor="#1E293B",
                    border_radius=20
                ),
                ft.Text("Build Your Future With Us", size=20, weight=ft.FontWeight.BOLD, color=TEXT_WHITE),
                ft.Text("Specialized in 20+ Final Year Diploma & B.Tech CSE Projects, E-Commerce platforms, and custom web apps.", size=13, color=TEXT_MUTED),
                ft.Row([
                    ft.ElevatedButton("Explore 20+ Projects", icon=ft.Icons.CODE, bgcolor=PRIMARY_COLOR, color="#000", on_click=lambda e: nav_to("projects")),
                    ft.OutlinedButton("Order Now", icon=ft.Icons.ADD_SHOPPING_CART, style=ft.ButtonStyle(color=PRIMARY_COLOR), on_click=lambda e: nav_to("order"))
                ], spacing=10, alignment=ft.MainAxisAlignment.START)
            ], spacing=10),
            padding=18,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#1E1B4B", "#0F172A"]
            ),
            border_radius=14,
            border=ft.border.all(1, "#312E81")
        )

        services_header = ft.Text("Our Core Services", size=15, weight=ft.FontWeight.BOLD, color=TEXT_WHITE)
        
        services_grid = ft.Column([
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.LAPTOP_MAC, color=PRIMARY_COLOR, size=24),
                    ft.Column([
                        ft.Text(s["name"], weight=ft.FontWeight.BOLD, color=TEXT_WHITE, size=12),
                        ft.Text(s["desc"], color=TEXT_MUTED, size=11)
                    ], spacing=2, expand=True)
                ], spacing=12),
                padding=12, bgcolor=CARD_BG, border_radius=10, border=ft.border.all(1, "#1E293B")
            ) for s in ADMIN_STORE["services"]
        ], spacing=8)

        content_area.controls.extend([hero, services_header, services_grid])

    # --- PROJECTS VIEW WITH MULTI-LINE TEXT WRAPPING ---
    def load_projects_view():
        header = ft.Column([
            ft.Text("🎓 Final Year Diploma & B.Tech CSE Projects", size=16, weight=ft.FontWeight.BOLD, color=TEXT_WHITE),
            ft.Text("Browse through our 20+ verified project ideas clearly. Click 'Order This Project' to proceed.", size=12, color=TEXT_MUTED),
            ft.Divider(color="#1E293B")
        ], spacing=6)

        proj_cards = ft.Column([
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Container(content=ft.Text(p["category"], size=10, color=PRIMARY_COLOR, weight=ft.FontWeight.BOLD), bgcolor="#1E293B", padding=5, border_radius=4),
                        ft.Text(p["price"], weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_ACCENT, size=13)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    # Enabled full multi-line wrapping so text never gets cut off
                    ft.Text(p["title"], weight=ft.FontWeight.BOLD, color=TEXT_WHITE, size=13, overflow=ft.TextOverflow.VISIBLE, max_lines=3),
                    ft.ElevatedButton("Order This Project", icon=ft.Icons.ARROW_FORWARD, bgcolor=PRIMARY_COLOR, color="#000", on_click=lambda e, title=p["title"]: nav_to("order"))
                ], spacing=8),
                padding=14, bgcolor=CARD_BG, border_radius=10, border=ft.border.all(1, "#1E293B")
            ) for p in ADMIN_STORE["projects"]
        ], spacing=12)

        content_area.controls.extend([header, proj_cards])

    def load_order_view():
        name_input = ft.TextField(label="Your Full Name", border_color=PRIMARY_COLOR, text_size=13, height=45, color=TEXT_WHITE)
        phone_input = ft.TextField(label="Mobile Number (e.g. 7995148054)", keyboard_type=ft.KeyboardType.PHONE, border_color=PRIMARY_COLOR, text_size=13, height=45, color=TEXT_WHITE)
        email_input = ft.TextField(label="Mail ID", keyboard_type=ft.KeyboardType.EMAIL, border_color=PRIMARY_COLOR, text_size=13, height=45, color=TEXT_WHITE)
        
        project_dropdown = ft.Dropdown(
            label="Select Project",
            border_color=PRIMARY_COLOR,
            text_size=12,
            color=TEXT_WHITE,
            bgcolor=CARD_BG,
            options=[ft.dropdown.Option(p["title"]) for p in ADMIN_STORE["projects"]]
        )

        def submit_order(e):
            if not name_input.value or not phone_input.value or not email_input.value or not project_dropdown.value:
                page.snack_bar = ft.SnackBar(ft.Text("Please fill all fields and select a project!"), bgcolor=ft.Colors.RED_900)
                page.snack_bar.open = True
                page.update()
                return
            
            new_order = {
                "id": f"ORD-{len(ADMIN_STORE['orders']) + 1001}",
                "type": "Project Order",
                "title": project_dropdown.value,
                "name": name_input.value,
                "phone": phone_input.value,
                "email": email_input.value,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "status": "Pending"
            }
            ADMIN_STORE["orders"].append(new_order)
            send_whatsapp_order(project_dropdown.value, name_input.value, phone_input.value, email_input.value)

        order_container = ft.Container(
            content=ft.Column([
                ft.Text("🛒 Secure Project Order Form", size=16, weight=ft.FontWeight.BOLD, color=TEXT_WHITE),
                ft.Text("Fill in your details below. Submitting will save your order and connect you instantly via WhatsApp (7995148054).", size=12, color=TEXT_MUTED),
                ft.Divider(color="#1E293B"),
                name_input,
                phone_input,
                email_input,
                project_dropdown,
                ft.Container(height=5),
                ft.ElevatedButton(
                    "Submit Order & Open WhatsApp", 
                    icon=ft.Icons.SEND, 
                    bgcolor="#25D366", 
                    color="#FFF", 
                    width=400,
                    on_click=submit_order
                )
            ], spacing=12),
            padding=18,
            bgcolor=CARD_BG,
            border_radius=12,
            border=ft.border.all(1, "#312E81")
        )

        content_area.controls.append(order_container)

    def load_shops_view():
        content_area.controls.append(ft.Text("🛍️ Shops & Hotels E-Commerce Portals", size=16, weight=ft.FontWeight.BOLD, color=TEXT_WHITE))
        content_area.controls.append(ft.Text("We build custom e-commerce websites and mobile ordering platforms for local shops, restaurants, and hotels.", size=12, color=TEXT_MUTED))
        
        shop_card = ft.Container(
            content=ft.Column([
                ft.Text("Hotel & Retail E-Commerce Package", weight=ft.FontWeight.BOLD, color=TEXT_WHITE, size=14),
                ft.Text("Includes dynamic menus, online cart, WhatsApp checkout, and admin dashboard.", size=11, color=TEXT_MUTED),
                ft.ElevatedButton("Inquire via WhatsApp", icon=ft.Icons.MESSAGE, bgcolor="#25D366", color="#FFF", on_click=lambda e: send_whatsapp_order("Shop E-Commerce Solution", "Client", "7995148054", "client@mail.com"))
            ], spacing=8),
            padding=15, bgcolor=CARD_BG, border_radius=10, border=ft.border.all(1, "#1E293B")
        )
        content_area.controls.append(shop_card)

    def load_reviews_view():
        content_area.controls.append(ft.Text("⭐ Customer Reviews & Testimonials", size=16, weight=ft.FontWeight.BOLD, color=TEXT_WHITE))
        
        r_name = ft.TextField(label="Your Name", border_color=PRIMARY_COLOR, text_size=12, height=40, color=TEXT_WHITE)
        r_comment = ft.TextField(label="Write your review...", multiline=True, border_color=PRIMARY_COLOR, text_size=12, min_lines=2, max_lines=3, color=TEXT_WHITE)
        
        def submit_review(e):
            if not r_name.value or not r_comment.value:
                return
            ADMIN_STORE["reviews"].insert(0, {"name": r_name.value, "rating": "★★★★★", "comment": r_comment.value})
            nav_to("reviews")
            page.snack_bar = ft.SnackBar(ft.Text("Review submitted successfully!"), bgcolor=ft.Colors.GREEN_900)
            page.snack_bar.open = True
            page.update()

        content_area.controls.extend([
            r_name, r_comment,
            ft.ElevatedButton("Post Review", icon=ft.Icons.STAR, bgcolor=PRIMARY_COLOR, color="#000", on_click=submit_review),
            ft.Divider(color="#1E293B")
        ])

        for r in ADMIN_STORE["reviews"]:
            content_area.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(r["name"], weight=ft.FontWeight.BOLD, color=TEXT_WHITE, size=12),
                            ft.Text(r["rating"], color=ft.colors.AMBER, size=11)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(r["comment"], color=TEXT_MUTED, size=11)
                    ], spacing=4),
                    padding=12, bgcolor=CARD_BG, border_radius=8, border=ft.border.all(1, "#1E293B")
                )
            )

    def load_admin_view():
        content_area.controls.append(
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, icon_color=PRIMARY_COLOR, on_click=lambda e: nav_to("home")),
                ft.Text("🛠️ Admin Panel - Stored Orders", size=16, weight=ft.FontWeight.BOLD, color=TEXT_WHITE)
            ], spacing=5)
        )
        content_area.controls.append(ft.Text(f"Total Orders Stored: {len(ADMIN_STORE['orders'])}", size=12, color=TEXT_MUTED))
        
        if not ADMIN_STORE["orders"]:
            content_area.controls.append(ft.Text("No orders recorded yet.", color=TEXT_MUTED, size=12))
            return

        for o in ADMIN_STORE["orders"]:
            content_area.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(o["id"], weight=ft.FontWeight.BOLD, color=PRIMARY_COLOR, size=12),
                            ft.Text(o["status"], color=ft.Colors.GREEN_ACCENT, size=11)
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(o["title"], weight=ft.FontWeight.BOLD, color=TEXT_WHITE, size=13),
                        ft.Text(f"Customer: {o['name']} | Mobile: {o['phone']}", color=TEXT_MUTED, size=11),
                        ft.Text(f"Email: {o['email']} | Date: {o['date']}", color=TEXT_MUTED, size=11)
                    ], spacing=4),
                    padding=14, bgcolor=CARD_BG, border_radius=10, border=ft.border.all(1, "#1E293B")
                )
            )

    load_home_view()

    page.add(
        ft.Container(
            content=ft.Column([
                app_bar,
                ft.Container(content=content_area, padding=14, expand=True),
                nav_bar
            ], spacing=0),
            width=420,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
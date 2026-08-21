import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, timedelta
import json
import os

# =========================================================
# SCHOOL PLANNER
# Python + Tkinter
# =========================================================

DATA_FILE = "school_planner_data.json"

BG = "#F5F7FB"
WHITE = "#FFFFFF"
PURPLE = "#6C5CE7"
PURPLE_DARK = "#5848D6"
PURPLE_LIGHT = "#EEEAFE"
TEXT = "#25243A"
GRAY = "#77758A"
BORDER = "#E7E8F0"
GREEN = "#35B879"
ORANGE = "#F59E0B"
BLUE = "#3B82F6"
RED = "#EF4444"

# =========================================================
# ข้อมูล
# =========================================================

data = {
    "tasks": [],
    "events": []
}


def load_data():
    global data

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)

            for key in data:
                if key in saved:
                    data[key] = saved[key]

        except Exception:
            pass


def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=2
        )


load_data()

# =========================================================
# ตารางเรียน
# เวลาเริ่ม-จบของแต่ละคาบ
# =========================================================

SCHEDULE = {

    "จันทร์": [
        ("08:30", "09:20", "ว31295", "ครูนฤมล", "com4"),
        ("09:20", "10:10", "ว31295", "ครูนฤมล", "com4"),
        ("10:10", "11:00", "ก31901", "ครูอภิญญา", "134"),
        ("11:00", "11:50", "พักกลางวัน", "", ""),
        ("11:50", "12:40", "ค31201", "ครูปาลีภัสร์", "134"),
        ("12:40", "13:30", "ค31201", "ครูปาลีภัสร์", "134"),
        ("13:30", "14:20", "ว31141", "ครูอุมาพร", "134"),
        ("14:30", "15:20", "ว31141", "ครูอุมาพร", "134"),
    ],

    "อังคาร": [
        ("08:30", "09:20", "ค31101", "ครูปาลีภัสร์", "134"),
        ("09:20", "10:10", "ค31101", "ครูปาลีภัสร์", "134"),
        ("10:10", "11:00", "อ31205", "ครูจินตนา", "134"),
        ("11:00", "11:50", "พักกลางวัน", "", ""),
        ("11:50", "12:40", "ท31101", "ครูศิริวรรณ", "134"),
        ("12:40", "13:30", "ท31101", "ครูศิริวรรณ", "R622"),
        ("13:30", "14:20", "พ31101", "ครูรัตน์ชนก", "134"),
        ("14:30", "15:20", "ส31101", "ครูวราภรณ์", "134"),
    ],

    "พุธ": [
        ("08:30", "09:20", "ประชุม", "", ""),
        ("09:20", "10:10", "ค31201", "ครูปาลีภัสร์", "134"),
        ("10:10", "11:00", "ค31201", "ครูปาลีภัสร์", "134"),
        ("11:00", "11:50", "พักกลางวัน", "", ""),
        ("11:50", "12:40", "ว31201", "ครูสุภกร", "Lab3"),
        ("12:40", "13:30", "ว31201", "ครูสุภกร", "Lab3"),
        ("13:30", "14:20", "ท31101", "ครูศิริวรรณ", "134"),
        ("14:30", "15:20", "ชุมนุม", "", ""),
    ],

    "พฤหัสฯ": [
        ("08:30", "09:20", "อ31101", "ครูJack Jalem", "134"),
        ("09:20", "10:10", "ว31221", "ครูเกศนก", "134"),
        ("10:10", "11:00", "ว31221", "ครูเกศนก", "134"),
        ("11:00", "11:50", "พักกลางวัน", "", ""),
        ("11:50", "12:40", "ง31101", "ครูวิรศรา", "134"),
        ("12:40", "13:30", "ว31295", "ครูนฤมล", "com4"),
        ("13:30", "14:20", "ว31295", "ครูนฤมล", "com4"),
        ("14:30", "15:20", "อ31101", "ครูศุภวัฒน์", "134"),
    ],

    "ศุกร์": [
        ("08:30", "09:20", "จิตสาธารณะ", "", ""),
        ("09:20", "10:10", "ว31221", "ครูเกศนก", "Lab7"),
        ("10:10", "11:00", "ส31102", "ครูศิริวรรณ", "134"),
        ("11:00", "11:50", "พักกลางวัน", "", ""),
        ("11:50", "12:40", "ว31201", "ครูสุภกร", "134"),
        ("12:40", "13:30", "ส31101", "ครูวราภรณ์", "134"),
        ("13:30", "14:20", "พ30237", "ครูพรนิภา", "อาคาร9"),
        ("14:30", "15:20", "ว31093", "ครูทินกร", "com1"),
    ]
}

# =========================================================
# วันหยุด
# =========================================================

WEEKEND_DAYS = {
    "เสาร์",
    "อาทิตย์"
}


def is_weekend(d):
    return d.weekday() >= 5


def get_schedule_for_date(d):
    """
    ถ้าเป็นเสาร์/อาทิตย์ ให้คืนค่าว่าง
    เพื่อไม่ให้แสดงตารางเรียน
    """
    if is_weekend(d):
        return []

    return SCHEDULE.get(
        day_name(d),
        []
    )


# =========================================================
# หน้าต่างหลัก
# =========================================================

root = tk.Tk()
root.title("School Planner")
root.geometry("1280x780")
root.minsize(1050, 650)
root.configure(bg=BG)

current_date = date.today()

# =========================================================
# ฟังก์ชันวันที่
# =========================================================

def thai_date(d):

    days = [
        "วันจันทร์",
        "วันอังคาร",
        "วันพุธ",
        "วันพฤหัสบดี",
        "วันศุกร์",
        "วันเสาร์",
        "วันอาทิตย์"
    ]

    months = [
        "",
        "มกราคม",
        "กุมภาพันธ์",
        "มีนาคม",
        "เมษายน",
        "พฤษภาคม",
        "มิถุนายน",
        "กรกฎาคม",
        "สิงหาคม",
        "กันยายน",
        "ตุลาคม",
        "พฤศจิกายน",
        "ธันวาคม"
    ]

    return (
        f"{days[d.weekday()]} "
        f"{d.day} "
        f"{months[d.month]} "
        f"{d.year + 543}"
    )


def day_name(d):

    names = [
        "จันทร์",
        "อังคาร",
        "พุธ",
        "พฤหัสฯ",
        "ศุกร์",
        "เสาร์",
        "อาทิตย์"
    ]

    return names[d.weekday()]


def change_day(amount):

    global current_date

    current_date += timedelta(days=amount)

    refresh_page()


def go_today():

    global current_date

    current_date = date.today()

    refresh_page()


def go_tomorrow():

    global current_date

    current_date = date.today() + timedelta(days=1)

    refresh_page()


# =========================================================
# Style
# =========================================================

style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass

style.configure(
    "Planner.Treeview",
    background=WHITE,
    fieldbackground=WHITE,
    foreground=TEXT,
    rowheight=58,
    borderwidth=0,
    font=("Tahoma", 10)
)

style.configure(
    "Planner.Treeview.Heading",
    background="#F7F7FB",
    foreground=GRAY,
    font=("Tahoma", 10, "bold"),
    relief="flat",
    padding=12
)

style.map(
    "Planner.Treeview",
    background=[
        ("selected", PURPLE_LIGHT)
    ],
    foreground=[
        ("selected", TEXT)
    ]
)

# =========================================================
# Sidebar
# =========================================================

sidebar = tk.Frame(
    root,
    bg=WHITE,
    width=235
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)

logo = tk.Frame(
    sidebar,
    bg=WHITE
)

logo.pack(
    fill="x",
    pady=25
)

tk.Label(
    logo,
    text="📚",
    font=("Arial", 30),
    bg=WHITE
).pack()

tk.Label(
    logo,
    text="School Planner",
    font=("Tahoma", 18, "bold"),
    fg=TEXT,
    bg=WHITE
).pack()

tk.Label(
    logo,
    text="ตารางเรียนของฉัน",
    font=("Tahoma", 9),
    fg=GRAY,
    bg=WHITE
).pack(
    pady=(3, 0)
)


def menu_button(text, command):

    btn = tk.Button(
        sidebar,
        text=text,
        command=command,
        font=("Tahoma", 10, "bold"),
        fg=TEXT,
        bg=WHITE,
        activebackground=PURPLE_LIGHT,
        activeforeground=PURPLE,
        relief="flat",
        bd=0,
        anchor="w",
        padx=25,
        pady=14,
        cursor="hand2"
    )

    btn.pack(
        fill="x",
        padx=12,
        pady=3
    )

    return btn


# =========================================================
# Content
# =========================================================

content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================================================
# Header
# =========================================================

header = tk.Frame(
    content,
    bg=WHITE,
    height=72
)

header.pack(
    fill="x"
)

header.pack_propagate(False)

tk.Label(
    header,
    text="School Planner",
    font=("Tahoma", 20, "bold"),
    fg=TEXT,
    bg=WHITE
).pack(
    side="left",
    padx=28
)

tk.Button(
    header,
    text="＋ เพิ่มข้อมูล",
    command=lambda: add_data_window(),
    font=("Tahoma", 10, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activebackground=PURPLE_DARK,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=18,
    pady=9
).pack(
    side="right",
    padx=25
)


# =========================================================
# Page
# =========================================================

page = tk.Frame(
    content,
    bg=BG
)

page.pack(
    fill="both",
    expand=True,
    padx=28,
    pady=25
)


def clear_page():

    for widget in page.winfo_children():
        widget.destroy()


# =========================================================
# Navigation
# =========================================================

def show_home():
    clear_page()
    build_home()


def show_schedule():
    clear_page()
    build_schedule()


def show_tasks():
    clear_page()
    build_tasks()


def show_events():
    clear_page()
    build_events()


menu_button(
    "🏠   หน้าแรก",
    show_home
)

menu_button(
    "📅   ตารางเรียน",
    show_schedule
)

menu_button(
    "📝   งานที่ต้องส่ง",
    show_tasks
)

menu_button(
    "📌   กำหนดการ",
    show_events
)

# =========================================================
# Card
# =========================================================

def make_card(
    parent,
    title,
    value,
    icon,
    color
):

    frame = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    icon_box = tk.Frame(
        frame,
        bg=color,
        width=50,
        height=50
    )

    icon_box.pack(
        side="left",
        padx=15,
        pady=15
    )

    icon_box.pack_propagate(False)

    tk.Label(
        icon_box,
        text=icon,
        font=("Arial", 21),
        fg=WHITE,
        bg=color
    ).pack(
        expand=True
    )

    info = tk.Frame(
        frame,
        bg=WHITE
    )

    info.pack(
        side="left",
        pady=12
    )

    tk.Label(
        info,
        text=title,
        font=("Tahoma", 9),
        fg=GRAY,
        bg=WHITE
    ).pack(
        anchor="w"
    )

    tk.Label(
        info,
        text=str(value),
        font=("Tahoma", 19, "bold"),
        fg=TEXT,
        bg=WHITE
    ).pack(
        anchor="w"
    )

    return frame


# =========================================================
# ข้อความวันหยุด
# =========================================================

def build_weekend_message(parent):

    box = tk.Frame(
        parent,
        bg=PURPLE_LIGHT,
        highlightbackground="#DDD7FF",
        highlightthickness=1
    )

    box.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    tk.Label(
        box,
        text="🎉",
        font=("Arial", 45),
        bg=PURPLE_LIGHT
    ).pack(
        pady=(45, 5)
    )

    tk.Label(
        box,
        text="วันนี้ไม่มีตารางเรียน",
        font=("Tahoma", 20, "bold"),
        fg=PURPLE,
        bg=PURPLE_LIGHT
    ).pack()

    tk.Label(
        box,
        text="เป็นวันเสาร์หรือวันอาทิตย์",
        font=("Tahoma", 11),
        fg=GRAY,
        bg=PURPLE_LIGHT
    ).pack(
        pady=5
    )

    tk.Label(
        box,
        text="พักผ่อนให้เต็มที่นะ 😊",
        font=("Tahoma", 11),
        fg=TEXT,
        bg=PURPLE_LIGHT
    ).pack(
        pady=(0, 35)
    )


# =========================================================
# หน้าแรก
# =========================================================

def build_home():

    tk.Label(
        page,
        text="สวัสดี 👋",
        font=("Tahoma", 26, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        anchor="w"
    )

    tk.Label(
        page,
        text=thai_date(current_date),
        font=("Tahoma", 11),
        fg=GRAY,
        bg=BG
    ).pack(
        anchor="w",
        pady=(2, 18)
    )

    # Cards

    cards = tk.Frame(
        page,
        bg=BG
    )

    cards.pack(
        fill="x",
        pady=(0, 20)
    )

    today_key = current_date.isoformat()

    lesson_count = len(
        get_schedule_for_date(
            current_date
        )
    )

    task_count = len([
        x for x in data["tasks"]
        if x.get("date") == today_key
    ])

    event_count = len([
        x for x in data["events"]
        if x.get("date") == today_key
    ])

    make_card(
        cards,
        "คาบเรียนวันนี้",
        lesson_count,
        "📅",
        PURPLE
    ).pack(
        side="left",
        fill="x",
        expand=True,
        padx=(0, 8)
    )

    make_card(
        cards,
        "งานที่ต้องส่ง",
        task_count,
        "📝",
        ORANGE
    ).pack(
        side="left",
        fill="x",
        expand=True,
        padx=8
    )

    make_card(
        cards,
        "กำหนดการ",
        event_count,
        "📌",
        BLUE
    ).pack(
        side="left",
        fill="x",
        expand=True,
        padx=(8, 0)
    )

    # ตารางวันนี้

    box = tk.Frame(
        page,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    box.pack(
        fill="both",
        expand=True
    )

    top = tk.Frame(
        box,
        bg=WHITE
    )

    top.pack(
        fill="x"
    )

    tk.Label(
        top,
        text="📅 ตารางเรียนวันนี้",
        font=("Tahoma", 15, "bold"),
        fg=TEXT,
        bg=WHITE
    ).pack(
        side="left",
        padx=20,
        pady=18
    )

    # ปุ่มวันนี้

    tk.Button(
        top,
        text="วันนี้",
        command=go_today,
        font=("Tahoma", 9, "bold"),
        fg=PURPLE,
        bg=PURPLE_LIGHT,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=12,
        pady=6
    ).pack(
        side="right",
        padx=(5, 20)
    )

    # ปุ่มพรุ่งนี้

    tk.Button(
        top,
        text="พรุ่งนี้ →",
        command=go_tomorrow,
        font=("Tahoma", 9, "bold"),
        fg=WHITE,
        bg=PURPLE,
        activebackground=PURPLE_DARK,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=12,
        pady=6
    ).pack(
        side="right"
    )

    # ถ้าเป็นเสาร์อาทิตย์

    if is_weekend(current_date):

        build_weekend_message(
            box
        )

        return

    tree = ttk.Treeview(
        box,
        columns=(
            "time",
            "subject",
            "teacher",
            "room"
        ),
        show="headings",
        style="Planner.Treeview"
    )

    tree.heading(
        "time",
        text="เวลา"
    )

    tree.heading(
        "subject",
        text="วิชา"
    )

    tree.heading(
        "teacher",
        text="ครูผู้สอน"
    )

    tree.heading(
        "room",
        text="ห้อง"
    )

    tree.column(
        "time",
        width=125,
        anchor="center"
    )

    tree.column(
        "subject",
        width=180,
        anchor="w"
    )

    tree.column(
        "teacher",
        width=280,
        anchor="w"
    )

    tree.column(
        "room",
        width=120,
        anchor="center"
    )

    tree.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=(0, 15)
    )

    rows = get_schedule_for_date(
        current_date
    )

    for item in rows:

        start, end, subject, teacher, room = item

        tree.insert(
            "",
            "end",
            values=(
                f"{start} - {end}",
                subject,
                teacher,
                room
            ),
            tags=(
                "break"
                if subject == "พักกลางวัน"
                else "normal"
            )
        )

    tree.tag_configure(
        "break",
        background="#FFF8E7",
        foreground="#9A6700"
    )


# =========================================================
# หน้าตารางเรียน
# =========================================================

def build_schedule():

    title = tk.Frame(
        page,
        bg=BG
    )

    title.pack(
        fill="x",
        pady=(0, 18)
    )

    tk.Label(
        title,
        text="📅 ตารางเรียน",
        font=("Tahoma", 26, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        side="left"
    )

    tk.Label(
        title,
        text=thai_date(current_date),
        font=("Tahoma", 11),
        fg=GRAY,
        bg=BG
    ).pack(
        side="right",
        pady=10
    )

    # -----------------------------------------------------
    # ปุ่มวัน
    # -----------------------------------------------------

    day_bar = tk.Frame(
        page,
        bg=BG
    )

    day_bar.pack(
        fill="x",
        pady=(0, 15)
    )

    days = [
        ("จันทร์", 0),
        ("อังคาร", 1),
        ("พุธ", 2),
        ("พฤหัสฯ", 3),
        ("ศุกร์", 4)
    ]

    for name, number in days:

        def choose(
            n=number
        ):

            global current_date

            monday = (
                current_date
                - timedelta(
                    days=current_date.weekday()
                )
            )

            current_date = (
                monday
                + timedelta(days=n)
            )

            refresh_page()

        active = (
            current_date.weekday()
            == number
        )

        tk.Button(
            day_bar,
            text=name,
            command=choose,
            font=("Tahoma", 10, "bold"),
            fg=WHITE if active else PURPLE,
            bg=PURPLE if active else WHITE,
            activebackground=PURPLE_DARK,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=25,
            pady=9
        ).pack(
            side="left",
            padx=4
        )

    # -----------------------------------------------------
    # ถ้าเป็นวันหยุด
    # -----------------------------------------------------

    if is_weekend(current_date):

        weekend = tk.Frame(
            page,
            bg=PURPLE_LIGHT,
            highlightbackground="#DDD7FF",
            highlightthickness=1
        )

        weekend.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            weekend,
            text="🎉",
            font=("Arial", 55),
            bg=PURPLE_LIGHT
        ).pack(
            pady=(90, 10)
        )

        tk.Label(
            weekend,
            text="ไม่มีตารางเรียน",
            font=("Tahoma", 24, "bold"),
            fg=PURPLE,
            bg=PURPLE_LIGHT
        ).pack()

        tk.Label(
            weekend,
            text="วันนี้เป็นวันเสาร์หรือวันอาทิตย์",
            font=("Tahoma", 12),
            fg=GRAY,
            bg=PURPLE_LIGHT
        ).pack(
            pady=8
        )

        tk.Button(
            weekend,
            text="กลับไปวันนี้",
            command=go_today,
            font=("Tahoma", 10, "bold"),
            fg=WHITE,
            bg=PURPLE,
            activebackground=PURPLE_DARK,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            pady=15
        )

        return

    # -----------------------------------------------------
    # ตารางเรียน
    # -----------------------------------------------------

    outer = tk.Frame(
        page,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    outer.pack(
        fill="both",
        expand=True
    )

    heading = tk.Frame(
        outer,
        bg="#F8F8FC",
        height=48
    )

    heading.pack(
        fill="x"
    )

    heading.pack_propagate(False)

    for text in [
        "เวลา",
        "วิชา",
        "ครูผู้สอน",
        "ห้อง"
    ]:

        tk.Label(
            heading,
            text=text,
            font=("Tahoma", 10, "bold"),
            fg=GRAY,
            bg="#F8F8FC",
            anchor="w"
        ).pack(
            side="left",
            fill="both",
            expand=True
        )

    canvas = tk.Canvas(
        outer,
        bg=WHITE,
        highlightthickness=0
    )

    scrollbar = ttk.Scrollbar(
        outer,
        orient="vertical",
        command=canvas.yview
    )

    body = tk.Frame(
        canvas,
        bg=WHITE
    )

    body.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=body,
        anchor="nw",
        width=850
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    rows = get_schedule_for_date(
        current_date
    )

    for item in rows:

        start, end, subject, teacher, room = item

        if subject == "พักกลางวัน":

            bg_color = "#FFF9EA"
            icon = "🍱"
            subject_color = "#A66B00"

        elif subject in (
            "ประชุม",
            "ชุมนุม",
            "จิตสาธารณะ"
        ):

            bg_color = "#F2F1FF"
            icon = "📌"
            subject_color = PURPLE

        else:

            bg_color = WHITE
            icon = "📖"
            subject_color = TEXT

        row = tk.Frame(
            body,
            bg=bg_color,
            height=70
        )

        row.pack(
            fill="x",
            pady=(0, 1)
        )

        row.pack_propagate(False)

        # เวลา

        time_box = tk.Frame(
            row,
            bg=bg_color
        )

        time_box.pack(
            side="left",
            fill="y",
            expand=True
        )

        tk.Label(
            time_box,
            text=f"{start}",
            font=("Tahoma", 10, "bold"),
            fg=TEXT,
            bg=bg_color
        ).pack(
            anchor="w",
            padx=10,
            pady=(12, 0)
        )

        tk.Label(
            time_box,
            text=f"{end}",
            font=("Tahoma", 8),
            fg=GRAY,
            bg=bg_color
        ).pack(
            anchor="w",
            padx=10
        )

        # วิชา

        subject_box = tk.Frame(
            row,
            bg=bg_color
        )

        subject_box.pack(
            side="left",
            fill="y",
            expand=True
        )

        tk.Label(
            subject_box,
            text=f"{icon}  {subject}",
            font=("Tahoma", 11, "bold"),
            fg=subject_color,
            bg=bg_color
        ).pack(
            anchor="w",
            padx=10,
            pady=22
        )

        # ครู

        teacher_box = tk.Frame(
            row,
            bg=bg_color
        )

        teacher_box.pack(
            side="left",
            fill="y",
            expand=True
        )

        tk.Label(
            teacher_box,
            text=teacher if teacher else "-",
            font=("Tahoma", 10),
            fg=TEXT,
            bg=bg_color
        ).pack(
            anchor="w",
            padx=10,
            pady=22
        )

        # ห้อง

        room_box = tk.Frame(
            row,
            bg=bg_color
        )

        room_box.pack(
            side="left",
            fill="y",
            expand=True
        )

        room_text = (
            f"ห้อง {room}"
            if room
            else "-"
        )

        tk.Label(
            room_box,
            text=room_text,
            font=("Tahoma", 9, "bold"),
            fg=PURPLE if room else GRAY,
            bg=bg_color
        ).pack(
            anchor="w",
            padx=10,
            pady=22
        )


# =========================================================
# งาน
# =========================================================

def build_tasks():

    tk.Label(
        page,
        text="📝 งานที่ต้องส่ง",
        font=("Tahoma", 26, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        anchor="w"
    )

    tk.Label(
        page,
        text="รวมงานทั้งหมดของคุณ",
        font=("Tahoma", 11),
        fg=GRAY,
        bg=BG
    ).pack(
        anchor="w",
        pady=(3, 18)
    )

    box = tk.Frame(
        page,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    box.pack(
        fill="both",
        expand=True
    )

    tree = ttk.Treeview(
        box,
        columns=(
            "date",
            "subject",
            "task",
            "due"
        ),
        show="headings",
        style="Planner.Treeview"
    )

    for c, h, w in [
        ("date", "วันที่", 150),
        ("subject", "วิชา", 180),
        ("task", "งานที่ต้องส่ง", 450),
        ("due", "กำหนดส่ง", 180)
    ]:

        tree.heading(
            c,
            text=h
        )

        tree.column(
            c,
            width=w
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    for item in data["tasks"]:

        tree.insert(
            "",
            "end",
            values=(
                item.get("date", ""),
                item.get("subject", ""),
                item.get("task", ""),
                item.get("due", "")
            )
        )


# =========================================================
# กำหนดการ
# =========================================================

def build_events():

    tk.Label(
        page,
        text="📌 กำหนดการ",
        font=("Tahoma", 26, "bold"),
        fg=TEXT,
        bg=BG
    ).pack(
        anchor="w"
    )

    tk.Label(
        page,
        text="กิจกรรมและกำหนดการต่าง ๆ",
        font=("Tahoma", 11),
        fg=GRAY,
        bg=BG
    ).pack(
        anchor="w",
        pady=(3, 18)
    )

    box = tk.Frame(
        page,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    box.pack(
        fill="both",
        expand=True
    )

    tree = ttk.Treeview(
        box,
        columns=(
            "date",
            "time",
            "title",
            "detail"
        ),
        show="headings",
        style="Planner.Treeview"
    )

    for c, h, w in [
        ("date", "วันที่", 150),
        ("time", "เวลา", 120),
        ("title", "กำหนดการ", 300),
        ("detail", "รายละเอียด", 400)
    ]:

        tree.heading(
            c,
            text=h
        )

        tree.column(
            c,
            width=w
        )

    tree.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    for item in data["events"]:

        tree.insert(
            "",
            "end",
            values=(
                item.get("date", ""),
                item.get("time", ""),
                item.get("title", ""),
                item.get("detail", "")
            )
        )


# =========================================================
# เพิ่มข้อมูล
# =========================================================

def add_data_window():

    win = tk.Toplevel(root)

    win.title("เพิ่มข้อมูล")

    win.geometry("570x560")

    win.configure(
        bg=WHITE
    )

    win.transient(root)

    win.grab_set()

    tk.Label(
        win,
        text="＋ เพิ่มข้อมูล",
        font=("Tahoma", 22, "bold"),
        fg=TEXT,
        bg=WHITE
    ).pack(
        pady=20
    )

    form = tk.Frame(
        win,
        bg=WHITE
    )

    form.pack(
        fill="both",
        expand=True,
        padx=35
    )

    fields = {}

    labels = [
        "ประเภท",
        "วันที่",
        "เวลา",
        "วิชา",
        "งาน",
        "กำหนดส่ง",
        "ชื่อกำหนดการ",
        "รายละเอียด"
    ]

    for i, label in enumerate(labels):

        tk.Label(
            form,
            text=label,
            font=("Tahoma", 10),
            fg=GRAY,
            bg=WHITE
        ).grid(
            row=i,
            column=0,
            sticky="w",
            pady=7
        )

        if label == "ประเภท":

            widget = ttk.Combobox(
                form,
                values=[
                    "งานที่ต้องส่ง",
                    "กำหนดการ"
                ],
                state="readonly",
                font=("Tahoma", 10)
            )

            widget.set(
                "งานที่ต้องส่ง"
            )

        else:

            widget = tk.Entry(
                form,
                font=("Tahoma", 10),
                relief="solid",
                bd=1
            )

        widget.grid(
            row=i,
            column=1,
            sticky="ew",
            padx=(20, 0),
            pady=7
        )

        fields[label] = widget

    form.columnconfigure(
        1,
        weight=1
    )

    fields["วันที่"].insert(
        0,
        current_date.isoformat()
    )

    def save():

        d = fields["วันที่"].get().strip()

        try:
            date.fromisoformat(d)

        except:

            messagebox.showerror(
                "วันที่ไม่ถูกต้อง",
                "กรุณาใช้รูปแบบ YYYY-MM-DD",
                parent=win
            )

            return

        typ = fields["ประเภท"].get()

        if typ == "งานที่ต้องส่ง":

            task = fields["งาน"].get().strip()

            if not task:

                messagebox.showwarning(
                    "ข้อมูลไม่ครบ",
                    "กรุณาใส่ชื่องาน",
                    parent=win
                )

                return

            data["tasks"].append({
                "date": d,
                "subject": fields["วิชา"].get().strip(),
                "task": task,
                "due": fields["กำหนดส่ง"].get().strip() or d
            })

        else:

            title = fields[
                "ชื่อกำหนดการ"
            ].get().strip()

            if not title:

                messagebox.showwarning(
                    "ข้อมูลไม่ครบ",
                    "กรุณาใส่ชื่อกำหนดการ",
                    parent=win
                )

                return

            data["events"].append({
                "date": d,
                "time": fields["เวลา"].get().strip(),
                "title": title,
                "detail": fields["รายละเอียด"].get().strip()
            })

        save_data()

        win.destroy()

        refresh_page()

    tk.Button(
        win,
        text="บันทึกข้อมูล",
        command=save,
        font=("Tahoma", 11, "bold"),
        fg=WHITE,
        bg=PURPLE,
        activebackground=PURPLE_DARK,
        relief="flat",
        bd=0,
        cursor="hand2",
        pady=11
    ).pack(
        fill="x",
        padx=35,
        pady=20
    )


# =========================================================
# Refresh
# =========================================================

def refresh_page():
    show_home()


# =========================================================
# เริ่มโปรแกรม
# =========================================================

show_home()

root.mainloop()
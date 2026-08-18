import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime, timedelta


# ============================================================
# ตั้งค่า
# ============================================================

DATA_FILE = "school_planner_data.json"

PURPLE = "#6D3FD1"
PURPLE_LIGHT = "#F1EAFF"
BG = "#F8F7FB"
WHITE = "#FFFFFF"
TEXT = "#241B32"
GRAY = "#81798C"
GREEN = "#35A66F"
RED = "#E05252"
ORANGE = "#E99A3D"


# ============================================================
# วัน / เดือน
# ============================================================

THAI_DAYS = [
    "จันทร์",
    "อังคาร",
    "พุธ",
    "พฤหัสฯ",
    "ศุกร์",
    "เสาร์",
    "อาทิตย์"
]

THAI_MONTHS = [
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


# ============================================================
# ตารางเรียน
# แก้ตารางตรงนี้ได้
# ============================================================

SCHEDULE = {

    "จันทร์": [
        ("08:30-09:20", "ว31295", "ครูณมล", "com4"),
        ("09:20-10:10", "ว31295", "ครูณมล", "com4"),
        ("10:10-11:00", "ก31901", "ครูอภิญญา", "134"),
        ("11:00-11:50", "พักกลางวัน", "", ""),
        ("11:50-12:40", "ค31201", "ครูปลิ๊คส์", "134"),
        ("12:40-13:30", "ค31201", "ครูปลิ๊คส์", "134"),
        ("13:30-14:20", "ว31141", "ครูอมาพร", "134"),
        ("14:30-15:20", "ว31141", "ครูอมาพร", "134"),
    ],

    "อังคาร": [
        ("08:30-09:20", "ค31101", "ครูปลิ๊คส์", "134"),
        ("09:20-10:10", "ค31101", "ครูปลิ๊คส์", "134"),
        ("10:10-11:00", "อ31205", "ครูจินตนา", "134"),
        ("11:00-11:50", "พักกลางวัน", "", ""),
        ("11:50-12:40", "ท31101", "ครูศรีประไพ", "134"),
        ("12:40-13:30", "ท31101", "ครูพลเดชรงค์", "R622"),
        ("13:30-14:20", "พ31101", "ครูรัตน์ชนก", "134"),
        ("14:30-15:20", "ส31101", "ครูวราภรณ์", "134"),
    ],

    "พุธ": [
        ("08:30-09:20", "ประชุม", "", ""),
        ("09:20-10:10", "ค31201", "ครูปลิ๊คส์", "134"),
        ("10:10-11:00", "ค31201", "ครูปลิ๊คส์", "134"),
        ("11:00-11:50", "พักกลางวัน", "", ""),
        ("11:50-12:40", "ว31201", "ครูสุภกร", "Lab3"),
        ("12:40-13:30", "ว31201", "ครูสุภกร", "Lab3"),
        ("13:30-14:20", "ท31101", "ครูศรีประไพ", "134"),
        ("14:30-15:20", "ชุมนุม", "", ""),
    ],

    "พฤหัสฯ": [
        ("08:30-09:20", "อ31101", "ครูJack Jalem", "134"),
        ("09:20-10:10", "ว31221", "ครูเกศนก", "134"),
        ("10:10-11:00", "ว31221", "ครูเกศนก", "134"),
        ("11:00-11:50", "พักกลางวัน", "", ""),
        ("11:50-12:40", "ง31101", "ครูวัชรา", "134"),
        ("12:40-13:30", "ว31295", "ครูณมล", "com4"),
        ("13:30-14:20", "ว31295", "ครูณมล", "com4"),
        ("14:30-15:20", "อ31101", "ครูศุภวัฒน์", "134"),
    ],

    "ศุกร์": [
        ("08:30-09:20", "จิตสาธารณะ", "", ""),
        ("09:20-10:10", "ว31221", "ครูเกศนก", "Lab7"),
        ("10:10-11:00", "ส31102", "ครูศรีวรรณ", "134"),
        ("11:00-11:50", "พักกลางวัน", "", ""),
        ("11:50-12:40", "ว31201", "ครูสุภกร", "134"),
        ("12:40-13:30", "ส31101", "ครูวราภรณ์", "134"),
        ("13:30-14:20", "พ30237", "ครูพรรณิภา", "อาคาร9"),
        ("14:30-15:20", "ว31093", "ครูทินกร", "com1"),
    ],
}


# ============================================================
# โหลด / บันทึกข้อมูล
# ============================================================

def load_data():

    if os.path.exists(DATA_FILE):

        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                result = json.load(file)

            if "tasks" not in result:
                result["tasks"] = []

            if "events" not in result:
                result["events"] = []

            return result

        except:
            pass

    return {
        "tasks": [],
        "events": []
    }


data = load_data()


def save_data():

    with open(
        DATA_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


# ============================================================
# แอป
# ============================================================

class SchoolPlanner:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "School Planner"
        )

        self.root.geometry(
            "1150x800"
        )

        self.root.minsize(
            900,
            600
        )

        self.root.configure(
            bg=BG
        )

        self.show_home()


    # ========================================================
    # วันที่
    # ========================================================

    def today(self):

        return datetime.now()


    def tomorrow(self):

        return datetime.now() + timedelta(days=1)


    def date_string(self, date):

        return date.strftime("%d/%m/%Y")


    def today_string(self):

        return self.date_string(
            self.today()
        )


    def tomorrow_string(self):

        return self.date_string(
            self.tomorrow()
        )


    def thai_date(self, date):

        return (
            f"{date.day} "
            f"{THAI_MONTHS[date.month - 1]} "
            f"{date.year + 543}"
        )


    # ========================================================
    # ล้างหน้าจอ
    # ========================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ========================================================
    # หน้าหลัก
    # ========================================================

    def show_home(self):

        self.clear()

        canvas = tk.Canvas(
            self.root,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            self.root,
            orient="vertical",
            command=canvas.yview
        )

        content = tk.Frame(
            canvas,
            bg=BG
        )

        content.bind(
            "<Configure>",
            lambda event:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw"
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


        # ====================================================
        # Header
        # ====================================================

        header = tk.Frame(
            content,
            bg=BG
        )

        header.pack(
            fill="x",
            padx=45,
            pady=(30, 10)
        )

        tk.Label(
            header,
            text="ตารางเรียนของฉัน",
            font=("Arial", 28, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text=(
                "วันนี้ • "
                + THAI_DAYS[self.today().weekday()]
                + " • "
                + self.thai_date(self.today())
            ),
            font=("Arial", 12),
            fg=PURPLE,
            bg=BG
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        tk.Label(
            header,
            text=(
                "พรุ่งนี้ • "
                + THAI_DAYS[self.tomorrow().weekday()]
                + " • "
                + self.thai_date(self.tomorrow())
            ),
            font=("Arial", 11),
            fg=GRAY,
            bg=BG
        ).pack(
            anchor="w"
        )


        # ====================================================
        # สรุป
        # ====================================================

        today_lessons = self.get_today_lessons()
        tomorrow_lessons = self.get_tomorrow_lessons()
        tomorrow_tasks = self.get_tomorrow_tasks()
        tomorrow_events = self.get_tomorrow_events()

        summary = tk.Frame(
            content,
            bg=BG
        )

        summary.pack(
            fill="x",
            padx=40,
            pady=15
        )

        self.summary_card(
            summary,
            "📚",
            str(len(today_lessons)),
            "คาบวันนี้"
        )

        self.summary_card(
            summary,
            "📚",
            str(len(tomorrow_lessons)),
            "คาบพรุ่งนี้"
        )

        self.summary_card(
            summary,
            "📝",
            str(len(tomorrow_tasks)),
            "งานพรุ่งนี้"
        )

        self.summary_card(
            summary,
            "📅",
            str(len(tomorrow_events)),
            "กำหนดการพรุ่งนี้"
        )


        # ====================================================
        # ตารางเรียนวันนี้
        # ====================================================

        self.section(
            content,
            "📚 ตารางเรียนวันนี้",
            "ตารางเรียนประจำวัน"
        )

        today_box = tk.Frame(
            content,
            bg=BG
        )

        today_box.pack(
            fill="x",
            padx=40
        )

        if not today_lessons:

            self.empty(
                today_box,
                "🎉 วันนี้ไม่มีเรียน"
            )

        else:

            for lesson in today_lessons:

                self.lesson_card(
                    today_box,
                    lesson
                )


        # ====================================================
        # ตารางเรียนพรุ่งนี้
        # ====================================================

        self.section(
            content,
            "📚 ตารางเรียนพรุ่งนี้",
            "ตารางเรียนประจำวัน"
        )

        tomorrow_box = tk.Frame(
            content,
            bg=BG
        )

        tomorrow_box.pack(
            fill="x",
            padx=40
        )

        if not tomorrow_lessons:

            self.empty(
                tomorrow_box,
                "🎉 พรุ่งนี้ไม่มีเรียน"
            )

        else:

            for lesson in tomorrow_lessons:

                self.lesson_card(
                    tomorrow_box,
                    lesson
                )


        # ====================================================
        # งานพรุ่งนี้
        # ====================================================

        self.section(
            content,
            "📝 งานที่ต้องส่งพรุ่งนี้",
            "ติ๊ก ✓ เมื่องานเสร็จแล้ว"
        )

        task_box = tk.Frame(
            content,
            bg=BG
        )

        task_box.pack(
            fill="x",
            padx=40
        )

        if not tomorrow_tasks:

            self.empty(
                task_box,
                "ยังไม่มีงานที่ต้องส่งพรุ่งนี้"
            )

        else:

            for task in tomorrow_tasks:

                self.task_card(
                    task_box,
                    task
                )


        # ====================================================
        # กำหนดการพรุ่งนี้
        # ====================================================

        self.section(
            content,
            "📅 กำหนดการพรุ่งนี้",
            "สอบ / กิจกรรม / นัดหมาย"
        )

        event_box = tk.Frame(
            content,
            bg=BG
        )

        event_box.pack(
            fill="x",
            padx=40
        )

        if not tomorrow_events:

            self.empty(
                event_box,
                "ยังไม่มีกำหนดการพรุ่งนี้"
            )

        else:

            for event in tomorrow_events:

                self.event_card(
                    event_box,
                    event
                )


        # ====================================================
        # ปุ่ม
        # ====================================================

        buttons = tk.Frame(
            content,
            bg=BG
        )

        buttons.pack(
            pady=30
        )

        tk.Button(
            buttons,
            text="+ เพิ่มงาน",
            command=self.add_task,
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PURPLE,
            activebackground=PURPLE,
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="+ เพิ่มกำหนดการ",
            command=self.add_event,
            font=("Arial", 11, "bold"),
            fg=PURPLE,
            bg=PURPLE_LIGHT,
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            buttons,
            text="📋 ดูทั้งหมด",
            command=self.show_all,
            font=("Arial", 11),
            fg=TEXT,
            bg=WHITE,
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10
        ).pack(
            side="left",
            padx=5
        )


    # ========================================================
    # Summary Card
    # ========================================================

    def summary_card(
        self,
        parent,
        icon,
        number,
        title
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#E5E0EA",
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            ipady=10
        )

        tk.Label(
            card,
            text=icon,
            font=("Arial", 21),
            bg=WHITE,
            fg=PURPLE
        ).pack(
            pady=(5, 0)
        )

        tk.Label(
            card,
            text=number,
            font=("Arial", 23, "bold"),
            bg=WHITE,
            fg=PURPLE
        ).pack()

        tk.Label(
            card,
            text=title,
            font=("Arial", 10),
            bg=WHITE,
            fg=GRAY
        ).pack(
            pady=(0, 7)
        )


    # ========================================================
    # Section
    # ========================================================

    def section(
        self,
        parent,
        title,
        subtitle=""
    ):

        frame = tk.Frame(
            parent,
            bg=BG
        )

        frame.pack(
            fill="x",
            padx=40,
            pady=(25, 8)
        )

        tk.Label(
            frame,
            text=title,
            font=("Arial", 20, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w"
        )

        if subtitle:

            tk.Label(
                frame,
                text=subtitle,
                font=("Arial", 10),
                fg=GRAY,
                bg=BG
            ).pack(
                anchor="w"
            )


    # ========================================================
    # Lesson Card
    # ========================================================

    def lesson_card(
        self,
        parent,
        lesson
    ):

        time, subject, teacher, room = lesson

        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#E5E0EA",
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=4
        )

        time_box = tk.Frame(
            card,
            bg=PURPLE_LIGHT,
            width=140
        )

        time_box.pack(
            side="left",
            fill="y"
        )

        time_box.pack_propagate(False)

        tk.Label(
            time_box,
            text=time,
            font=("Arial", 11, "bold"),
            fg=PURPLE,
            bg=PURPLE_LIGHT
        ).pack(
            expand=True
        )

        info = tk.Frame(
            card,
            bg=WHITE
        )

        info.pack(
            side="left",
            fill="both",
            expand=True,
            padx=18,
            pady=10
        )

        tk.Label(
            info,
            text=subject,
            font=("Arial", 15, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w"
        )

        if teacher:

            tk.Label(
                info,
                text=f"{teacher} • ห้อง {room}",
                font=("Arial", 10),
                fg=GRAY,
                bg=WHITE
            ).pack(
                anchor="w",
                pady=(3, 0)
            )

        elif subject == "พักกลางวัน":

            tk.Label(
                info,
                text="พักกลางวัน",
                font=("Arial", 10),
                fg=ORANGE,
                bg=WHITE
            ).pack(
                anchor="w"
            )


    # ========================================================
    # Task Card
    # ========================================================

    def task_card(
        self,
        parent,
        task
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#E5E0EA",
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=4
        )

        done = tk.BooleanVar(
            value=task.get(
                "done",
                False
            )
        )

        def toggle():

            task["done"] = done.get()

            save_data()

            self.show_home()

        tk.Checkbutton(
            card,
            variable=done,
            command=toggle,
            bg=WHITE,
            activebackground=WHITE,
            cursor="hand2"
        ).pack(
            side="left",
            padx=10
        )

        info = tk.Frame(
            card,
            bg=WHITE
        )

        info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=10
        )

        title = task.get(
            "title",
            "ไม่มีชื่อ"
        )

        if task.get("done"):
            title = "✓ " + title

        tk.Label(
            info,
            text=title,
            font=("Arial", 14, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            info,
            text=(
                task.get("subject", "ไม่ระบุวิชา")
                + " • กำหนดส่ง "
                + task.get("date", "")
            ),
            font=("Arial", 9),
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        priority = task.get(
            "priority",
            "ปกติ"
        )

        color = (
            RED
            if priority == "สูง"
            else ORANGE
            if priority == "ปานกลาง"
            else GREEN
        )

        tk.Label(
            card,
            text=priority,
            font=("Arial", 9, "bold"),
            fg=color,
            bg=WHITE
        ).pack(
            side="right",
            padx=15
        )

        tk.Button(
            card,
            text="ลบ",
            command=lambda t=task:
            self.delete_task(t),
            font=("Arial", 9),
            fg=WHITE,
            bg=RED,
            relief="flat",
            cursor="hand2"
        ).pack(
            side="right",
            padx=5
        )


    # ========================================================
    # Event Card
    # ========================================================

    def event_card(
        self,
        parent,
        event
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#E5E0EA",
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=4
        )

        tk.Label(
            card,
            text="📅",
            font=("Arial", 20),
            fg=PURPLE,
            bg=WHITE
        ).pack(
            side="left",
            padx=15
        )

        info = tk.Frame(
            card,
            bg=WHITE
        )

        info.pack(
            side="left",
            fill="both",
            expand=True,
            pady=10
        )

        tk.Label(
            info,
            text=event.get(
                "title",
                "กำหนดการ"
            ),
            font=("Arial", 14, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w"
        )

        details = (
            event.get("date", "")
            + " • "
            + event.get("time", "")
        )

        if event.get("detail"):
            details += " • " + event.get("detail")

        tk.Label(
            info,
            text=details,
            font=("Arial", 10),
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        tk.Button(
            card,
            text="ลบ",
            command=lambda e=event:
            self.delete_event(e),
            font=("Arial", 9),
            fg=WHITE,
            bg=RED,
            relief="flat",
            cursor="hand2"
        ).pack(
            side="right",
            padx=15
        )


    # ========================================================
    # Empty
    # ========================================================

    def empty(
        self,
        parent,
        text
    ):

        box = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#E5E0EA",
            highlightthickness=1
        )

        box.pack(
            fill="x",
            pady=4
        )

        tk.Label(
            box,
            text=text,
            font=("Arial", 11),
            fg=GRAY,
            bg=WHITE
        ).pack(
            pady=22
        )


    # ========================================================
    # ดึงตารางเรียน
    # ========================================================

    def get_today_lessons(self):

        weekday = self.today().weekday()

        if weekday >= 5:
            return []

        return SCHEDULE.get(
            THAI_DAYS[weekday],
            []
        )


    def get_tomorrow_lessons(self):

        weekday = self.tomorrow().weekday()

        if weekday >= 5:
            return []

        return SCHEDULE.get(
            THAI_DAYS[weekday],
            []
        )


    # ========================================================
    # ดึงงาน
    # ========================================================

    def get_tomorrow_tasks(self):

        target = self.tomorrow_string()

        return [
            task
            for task in data["tasks"]
            if task.get("date") == target
        ]


    # ========================================================
    # ดึงกำหนดการ
    # ========================================================

    def get_tomorrow_events(self):

        target = self.tomorrow_string()

        return [
            event
            for event in data["events"]
            if event.get("date") == target
        ]


    # ========================================================
    # เพิ่มงาน
    # ========================================================

    def add_task(self):

        win = tk.Toplevel(
            self.root
        )

        win.title(
            "เพิ่มงานที่ต้องส่ง"
        )

        win.geometry(
            "440x470"
        )

        win.configure(
            bg=WHITE
        )

        win.resizable(
            False,
            False
        )

        tk.Label(
            win,
            text="เพิ่มงานที่ต้องส่ง",
            font=("Arial", 21, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            pady=20
        )

        tk.Label(
            win,
            text="ชื่องาน",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30
        )

        title = tk.Entry(
            win,
            font=("Arial", 12)
        )

        title.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="กำหนดส่ง วัน/เดือน/ปี",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        date_entry = tk.Entry(
            win,
            font=("Arial", 12)
        )

        date_entry.insert(
            0,
            self.tomorrow_string()
        )

        date_entry.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="วิชา",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        subject = tk.Entry(
            win,
            font=("Arial", 12)
        )

        subject.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="ความสำคัญ",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        priority = tk.StringVar(
            value="ปกติ"
        )

        tk.OptionMenu(
            win,
            priority,
            "ต่ำ",
            "ปกติ",
            "ปานกลาง",
            "สูง"
        ).pack(
            anchor="w",
            padx=30
        )

        def save():

            name = title.get().strip()
            date_text = date_entry.get().strip()

            if not name:

                messagebox.showwarning(
                    "แจ้งเตือน",
                    "กรุณาใส่ชื่องาน"
                )

                return

            try:

                datetime.strptime(
                    date_text,
                    "%d/%m/%Y"
                )

            except ValueError:

                messagebox.showwarning(
                    "วันที่ไม่ถูกต้อง",
                    "ใช้รูปแบบ วัน/เดือน/ปี\nเช่น 18/08/2026"
                )

                return

            data["tasks"].append({
                "title": name,
                "date": date_text,
                "subject": subject.get().strip(),
                "priority": priority.get(),
                "done": False
            })

            save_data()

            win.destroy()

            self.show_home()

        tk.Button(
            win,
            text="บันทึกงาน",
            command=save,
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PURPLE,
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(
            fill="x",
            padx=30,
            pady=18
        )


    # ========================================================
    # เพิ่มกำหนดการ
    # ========================================================

    def add_event(self):

        win = tk.Toplevel(
            self.root
        )

        win.title(
            "เพิ่มกำหนดการ"
        )

        win.geometry(
            "440x500"
        )

        win.configure(
            bg=WHITE
        )

        win.resizable(
            False,
            False
        )

        tk.Label(
            win,
            text="เพิ่มกำหนดการ",
            font=("Arial", 21, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            pady=20
        )

        tk.Label(
            win,
            text="ชื่อกำหนดการ",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30
        )

        title = tk.Entry(
            win,
            font=("Arial", 12)
        )

        title.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="วันที่ วัน/เดือน/ปี",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        date_entry = tk.Entry(
            win,
            font=("Arial", 12)
        )

        date_entry.insert(
            0,
            self.tomorrow_string()
        )

        date_entry.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="เวลา HH:MM",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        time_entry = tk.Entry(
            win,
            font=("Arial", 12)
        )

        time_entry.insert(
            0,
            "08:00"
        )

        time_entry.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        tk.Label(
            win,
            text="รายละเอียด",
            fg=GRAY,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=30,
            pady=(10, 0)
        )

        detail = tk.Entry(
            win,
            font=("Arial", 12)
        )

        detail.pack(
            fill="x",
            padx=30,
            pady=5,
            ipady=7
        )

        def save():

            name = title.get().strip()
            date_text = date_entry.get().strip()
            time_text = time_entry.get().strip()

            if not name:

                messagebox.showwarning(
                    "แจ้งเตือน",
                    "กรุณาใส่ชื่อกำหนดการ"
                )

                return

            try:

                datetime.strptime(
                    date_text,
                    "%d/%m/%Y"
                )

            except ValueError:

                messagebox.showwarning(
                    "วันที่ไม่ถูกต้อง",
                    "ใช้รูปแบบ วัน/เดือน/ปี\nเช่น 25/08/2026"
                )

                return

            try:

                datetime.strptime(
                    time_text,
                    "%H:%M"
                )

            except ValueError:

                messagebox.showwarning(
                    "เวลาไม่ถูกต้อง",
                    "ใช้รูปแบบ HH:MM\nเช่น 08:30"
                )

                return

            data["events"].append({
                "title": name,
                "date": date_text,
                "time": time_text,
                "detail": detail.get().strip()
            })

            save_data()

            win.destroy()

            self.show_home()

        tk.Button(
            win,
            text="บันทึกกำหนดการ",
            command=save,
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PURPLE,
            relief="flat",
            cursor="hand2",
            pady=10
        ).pack(
            fill="x",
            padx=30,
            pady=18
        )


    # ========================================================
    # ลบงาน
    # ========================================================

    def delete_task(
        self,
        task
    ):

        answer = messagebox.askyesno(
            "ลบงาน",
            "ต้องการลบงานนี้หรือไม่?"
        )

        if answer:

            if task in data["tasks"]:

                data["tasks"].remove(
                    task
                )

                save_data()

                self.show_home()


    # ========================================================
    # ลบกำหนดการ
    # ========================================================

    def delete_event(
        self,
        event
    ):

        answer = messagebox.askyesno(
            "ลบกำหนดการ",
            "ต้องการลบกำหนดการนี้หรือไม่?"
        )

        if answer:

            if event in data["events"]:

                data["events"].remove(
                    event
                )

                save_data()

                self.show_home()


    # ========================================================
    # ดูทั้งหมด
    # ========================================================

    def show_all(self):

        win = tk.Toplevel(
            self.root
        )

        win.title(
            "งานและกำหนดการทั้งหมด"
        )

        win.geometry(
            "750x650"
        )

        win.configure(
            bg=BG
        )

        canvas = tk.Canvas(
            win,
            bg=BG,
            highlightthickness=0
        )

        scroll = tk.Scrollbar(
            win,
            orient="vertical",
            command=canvas.yview
        )

        content = tk.Frame(
            canvas,
            bg=BG
        )

        content.bind(
            "<Configure>",
            lambda e:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=content,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scroll.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scroll.pack(
            side="right",
            fill="y"
        )

        tk.Label(
            content,
            text="งานทั้งหมด",
            font=("Arial", 22, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        if not data["tasks"]:

            self.empty(
                content,
                "ยังไม่มีงาน"
            )

        else:

            for task in data["tasks"]:

                self.task_card(
                    content,
                    task
                )

        tk.Label(
            content,
            text="กำหนดการทั้งหมด",
            font=("Arial", 22, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            padx=25,
            pady=(30, 10)
        )

        if not data["events"]:

            self.empty(
                content,
                "ยังไม่มีกำหนดการ"
            )

        else:

            events = sorted(
                data["events"],
                key=lambda e: (
                    datetime.strptime(
                        e["date"],
                        "%d/%m/%Y"
                    ),
                    e.get(
                        "time",
                        "00:00"
                    )
                )
            )

            for event in events:

                self.event_card(
                    content,
                    event
                )


# ============================================================
# เริ่มโปรแกรม
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = SchoolPlanner(
        root
    )

    root.mainloop()
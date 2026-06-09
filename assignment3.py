# Student Name: [Your Name] | Assignment 3 | Python for Beginners

import tkinter as tk
from tkinter import messagebox

# ============================================================
# Step 1 — OOP Classes
# ============================================================

class Student:
    """Parent class representing a regular student."""

    def __init__(self, name, age, score, city):
        self.name = name
        self.age = age
        self.city = city
        self.__score = score  # private attribute

    # Getter
    def get_score(self):
        return self.__score

    # Setter with validation
    def set_score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            print("Error: Score must be between 0 and 100.")

    def get_grade(self):
        score = self.__score
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def is_pass(self):
        return self.__score >= 50

    def display(self):
        status = "Pass" if self.is_pass() else "Fail"
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"City  : {self.city}")
        print(f"Score : {self.__score:.2f}")
        print(f"Grade : {self.get_grade().upper()}")
        print(f"Status: {status}")

    def __str__(self):
        return f"Student: {self.name} | Score: {self.__score:.2f} | Grade: {self.get_grade().upper()}"


class GraduateStudent(Student):
    """Child class for graduate students with a thesis."""

    def __init__(self, name, age, score, city, thesis):
        super().__init__(name, age, score, city)
        self.thesis = thesis

    def display(self):
        super().display()
        print(f"Thesis: {self.thesis}")

    def __str__(self):
        return f"Graduate: {self.name} | Thesis: {self.thesis} | Grade: {self.get_grade().upper()}"


class PartTimeStudent(Student):
    """Child class for part-time students with a job."""

    def __init__(self, name, age, score, city, job):
        super().__init__(name, age, score, city)
        self.job = job

    def display(self):
        super().display()
        print(f"Job   : {self.job}")

    def __str__(self):
        return f"Part-Time: {self.name} | Job: {self.job} | Grade: {self.get_grade().upper()}"


# ============================================================
# Step 2 — String Methods (strip, title, upper, f-strings, split)
# are demonstrated throughout Steps 2, 3, and 4 as noted below.
# ============================================================

def clean_name(raw):
    """Apply .strip() and .title() to a name or city string."""
    return raw.strip().title()          # string method: strip() + title()


# ============================================================
# Step 3 — File Handling
# ============================================================

def save_to_file(students, filename):
    """Save a list of student objects to a CSV file."""
    with open(filename, "w") as f:
        for s in students:
            # Determine type and extra field
            if isinstance(s, GraduateStudent):       # check specific type first
                stype = "graduate"
                extra = s.thesis
            elif isinstance(s, PartTimeStudent):
                stype = "parttime"
                extra = s.job
            else:
                stype = "regular"
                extra = "none"
            # Write comma-separated line using f-string
            f.write(f"{s.name},{s.age},{s.get_score()},{s.city},{stype},{extra}\n")
    print(f"Data saved to {filename} successfully!")


def load_from_file(filename):
    """Load student objects from a CSV file and return as a list."""
    loaded = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()             # string method: strip()
                if not line:
                    continue
                fields = line.split(",")        # string method: split()
                name  = fields[0].strip().title()   # strip() + title()
                age   = int(fields[1].strip())
                score = float(fields[2].strip())
                city  = fields[3].strip().title()
                stype = fields[4].strip()
                extra = fields[5].strip()

                if stype == "graduate":
                    obj = GraduateStudent(name, age, score, city, extra)
                elif stype == "parttime":
                    obj = PartTimeStudent(name, age, score, city, extra)
                else:
                    obj = Student(name, age, score, city)
                loaded.append(obj)
    except FileNotFoundError:
        print("No saved data found.")
    return loaded


# ============================================================
# Step 4 — Tkinter GUI
# ============================================================

# Global student list
students = []
FILENAME = "students.txt"


def build_report():
    """Build the formatted report string for the Text widget."""
    if not students:
        return "No students added yet."

    lines = []
    lines.append("=" * 40)
    lines.append("       STUDENT REPORT SYSTEM       ")
    lines.append("=" * 40)

    for i, s in enumerate(students, start=1):
        # Use isinstance() — check most specific type first
        if isinstance(s, GraduateStudent):
            label = "Graduate Student"
            extra_line = f"   City: {s.city} | Thesis: {s.thesis}"
        elif isinstance(s, PartTimeStudent):
            label = "Part-Time Student"
            extra_line = f"   City: {s.city} | Job: {s.job}"
        else:
            label = "Regular Student"
            extra_line = f"   City: {s.city}"

        status = "Pass" if s.is_pass() else "Fail"
        # f-string with :.2f for decimal output; .upper() for grade
        lines.append(f"{i}. {s.name} [{label}]")
        lines.append(f"   Score: {s.get_score():.2f} | Grade: {s.get_grade().upper()} | {status}")
        lines.append(extra_line)
        lines.append("-" * 40)

    total   = len(students)
    passed  = sum(1 for s in students if s.is_pass())
    average = sum(s.get_score() for s in students) / total

    lines.append(f"Total Students : {total}")
    lines.append(f"Passed         : {passed}")
    lines.append(f"Class Average  : {average:.2f}")   # f-string with :.2f
    lines.append("=" * 40)

    return "\n".join(lines)


def refresh_display():
    """Clear and rewrite the Text widget with the current report."""
    txt_display.config(state=tk.NORMAL)
    txt_display.delete("1.0", tk.END)
    txt_display.insert(tk.END, build_report())
    txt_display.config(state=tk.DISABLED)


def add_student():
    """Validate inputs, create the correct student object, add to list."""
    name  = ent_name.get()
    age   = ent_age.get()
    score = ent_score.get()
    city  = ent_city.get()
    stype = var_type.get()
    extra = ent_extra.get()

    # --- Validation ---
    if not name.strip() or not age.strip() or not score.strip() or not city.strip():
        messagebox.showerror("Input Error", "All fields (Name, Age, Score, City) must be filled.")
        return

    if stype in ("Graduate", "Part-Time") and not extra.strip():
        messagebox.showerror("Input Error", "Please fill in the Thesis / Job field.")
        return

    try:
        age_val = int(age.strip())
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a valid whole number.")
        return

    try:
        score_val = float(score.strip())
    except ValueError:
        messagebox.showerror("Input Error", "Score must be a valid number.")
        return

    if not (0 <= score_val <= 100):
        messagebox.showerror("Input Error", "Score must be between 0 and 100.")
        return

    # Apply string methods: strip() + title()
    clean_n = clean_name(name)
    clean_c = clean_name(city)

    if stype == "Graduate":
        obj = GraduateStudent(clean_n, age_val, score_val, clean_c, extra.strip().title())
    elif stype == "Part-Time":
        obj = PartTimeStudent(clean_n, age_val, score_val, clean_c, extra.strip().title())
    else:
        obj = Student(clean_n, age_val, score_val, clean_c)

    students.append(obj)
    refresh_display()
    clear_form()


def save_students():
    """Save current students list to file."""
    if not students:
        messagebox.showwarning("Save", "No students to save.")
        return
    save_to_file(students, FILENAME)
    messagebox.showinfo("Save", f"Data saved to '{FILENAME}' successfully!")


def load_students():
    """Load students from file and refresh display."""
    global students
    loaded = load_from_file(FILENAME)
    if loaded:
        students = loaded
        refresh_display()
        messagebox.showinfo("Load", f"Loaded {len(loaded)} student(s) from '{FILENAME}'.")
    else:
        messagebox.showwarning("Load", "No saved data found.")


def clear_form():
    """Clear all entry fields."""
    ent_name.delete(0, tk.END)
    ent_age.delete(0, tk.END)
    ent_score.delete(0, tk.END)
    ent_city.delete(0, tk.END)
    ent_extra.delete(0, tk.END)
    var_type.set("Regular")
    toggle_extra()


def toggle_extra(*args):
    """Show/hide the Extra field depending on student type."""
    if var_type.get() in ("Graduate", "Part-Time"):
        lbl_extra.grid()
        ent_extra.grid()
        label_text = "Thesis:" if var_type.get() == "Graduate" else "Job Title:"
        lbl_extra.config(text=label_text)
    else:
        lbl_extra.grid_remove()
        ent_extra.grid_remove()


# ---- Build the main window ----
root = tk.Tk()
root.title("Student Report System")
root.resizable(False, False)

# ---- Section A: Input Form ----
frm_input = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
frm_input.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Title label
tk.Label(frm_input, text="Student Report System",
         font=("Arial", 14, "bold"), fg="blue").grid(row=0, column=0, columnspan=2, pady=(0, 8))

# Name
tk.Label(frm_input, text="Name:").grid(row=1, column=0, sticky="w", pady=3)
ent_name = tk.Entry(frm_input, width=30)
ent_name.grid(row=1, column=1, sticky="w", pady=3)

# Age
tk.Label(frm_input, text="Age:").grid(row=2, column=0, sticky="w", pady=3)
ent_age = tk.Entry(frm_input, width=30)
ent_age.grid(row=2, column=1, sticky="w", pady=3)

# Score
tk.Label(frm_input, text="Score:").grid(row=3, column=0, sticky="w", pady=3)
ent_score = tk.Entry(frm_input, width=30)
ent_score.grid(row=3, column=1, sticky="w", pady=3)

# City
tk.Label(frm_input, text="City:").grid(row=4, column=0, sticky="w", pady=3)
ent_city = tk.Entry(frm_input, width=30)
ent_city.grid(row=4, column=1, sticky="w", pady=3)

# Student Type
tk.Label(frm_input, text="Type:").grid(row=5, column=0, sticky="w", pady=3)
var_type = tk.StringVar(value="Regular")
var_type.trace("w", toggle_extra)
opt_type = tk.OptionMenu(frm_input, var_type, "Regular", "Graduate", "Part-Time")
opt_type.config(width=26)
opt_type.grid(row=5, column=1, sticky="w", pady=3)

# Extra (Thesis / Job) — hidden by default
lbl_extra = tk.Label(frm_input, text="Thesis:")
lbl_extra.grid(row=6, column=0, sticky="w", pady=3)
ent_extra = tk.Entry(frm_input, width=30)
ent_extra.grid(row=6, column=1, sticky="w", pady=3)
lbl_extra.grid_remove()
ent_extra.grid_remove()

# Buttons
frm_buttons = tk.Frame(frm_input)
frm_buttons.grid(row=7, column=0, columnspan=2, pady=(10, 0))

tk.Button(frm_buttons, text="Add Student",    width=14, bg="#4CAF50", fg="white",
          command=add_student).grid(row=0, column=0, padx=4)
tk.Button(frm_buttons, text="Save to File",   width=14, bg="#2196F3", fg="white",
          command=save_students).grid(row=0, column=1, padx=4)
tk.Button(frm_buttons, text="Load from File", width=14, bg="#FF9800", fg="white",
          command=load_students).grid(row=0, column=2, padx=4)
tk.Button(frm_buttons, text="Clear Form",     width=14, bg="#9E9E9E", fg="white",
          command=clear_form).grid(row=0, column=3, padx=4)

# ---- Section B: Results Display ----
frm_display = tk.LabelFrame(root, text="Report", padx=10, pady=10)
frm_display.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")

txt_display = tk.Text(frm_display, width=60, height=20, font=("Courier", 10),
                      state=tk.DISABLED, bg="#f9f9f9")
txt_display.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(frm_display, command=txt_display.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
txt_display.config(yscrollcommand=scrollbar.set)

# ---- Start the application ----
refresh_display()
root.mainloop()
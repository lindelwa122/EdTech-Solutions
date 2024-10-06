import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edtech.settings')

import django
django.setup()

from models import *

# Delete everything
courses = Course.objects.all()
for c in courses: c.delete()

lessons = Lesson.objects.all()
for l in lessons: l.delete()

# Create 2 courses
termux = Course.objects.create(name='Working with Termux')
programming = Course.objects.create(name='Introduction to Programming')

# Create termux lessons
termux_lessons = [
    """<div>
    <h1>What is Termux?</h1>
    <p>Termux is a powerful terminal emulator for Android that provides a Linux environment. It allows users to access a command line interface, run scripts, and install a wide range of software packages.</p>
    <p>With Termux, you can:</p>
    <ul>
        <li>Run Linux command-line tools.</li>
        <li>Access Android's underlying features and functions.</li>
        <li>Install programming languages like Python, Ruby, and Node.js.</li>
    </ul>
    <img src="https://example.com/termux_intro.jpg" alt="Termux Intro" style="max-width:100%;">
</div>
""",
"""<div>
    <h1>Simple Termux Commands</h1>
    <p>Here are some basic commands to get you started with Termux:</p>
    <table border="1" style="width:100%; text-align:left;">
        <tr>
            <th>Command</th>
            <th>Description</th>
        </tr>
        <tr>
            <td><code>ls</code></td>
            <td>Lists files and directories in the current directory.</td>
        </tr>
        <tr>
            <td><code>cd</code> [directory]</td>
            <td>Changes the current directory to the specified one.</td>
        </tr>
        <tr>
            <td><code>pwd</code></td>
            <td>Prints the current working directory.</td>
        </tr>
        <tr>
            <td><code>mkdir</code> [directory]</td>
            <td>Creates a new directory.</td>
        </tr>
        <tr>
            <td><code>rm</code> [file]</td>
            <td>Removes a file or directory.</td>
        </tr>
    </table>
    <img src="https://example.com/termux_commands.jpg" alt="Termux Commands" style="max-width:100%;">
</div>
""",
"""<div>
    <h1>Use Python on Termux</h1>
    <p>Termux allows you to run Python scripts directly from your mobile device.</p>
    <h2>Installing Python</h2>
    <p>To install Python, use the following command:</p>
    <code>pkg install python</code>
    <h2>Running Python Scripts</h2>
    <p>After installation, you can start Python by typing:</p>
    <code>python</code>
    <p>To run a Python script (e.g., <code>script.py</code>):</p>
    <code>python script.py</code>
    <h2>Creating a Simple Script</h2>
    <p>Here's a simple Python script you can create:</p>
    <pre><code>print("Hello, Termux!")</code></pre>
    <img src="https://example.com/termux_python.jpg" alt="Python in Termux" style="max-width:100%;">
</div>
""",
"""<div>
    <h1>Use Python on Termux</h1>
    <p>Termux allows you to run Python scripts directly from your mobile device.</p>
    <h2>Installing Python</h2>
    <p>To install Python, use the following command:</p>
    <code>pkg install python</code>
    <h2>Running Python Scripts</h2>
    <p>After installation, you can start Python by typing:</p>
    <code>python</code>
    <p>To run a Python script (e.g., <code>script.py</code>):</p>
    <code>python script.py</code>
    <h2>Creating a Simple Script</h2>
    <p>Here's a simple Python script you can create:</p>
    <pre><code>print("Hello, Termux!")</code></pre>
    <img src="https://example.com/termux_python.jpg" alt="Python in Termux" style="max-width:100%;">
</div>
"""
]

termux_lesson_title = [
    'What is Termux?',
 'Simple Termux commands.',
 'How to install packages?',
'Use Python on Termux.',
]

for i in range(4):
    l = Lesson.objects.create(title=termux_lesson_title[i], content=termux_lessons[i], course=termux)
    l.save()

programming_titles = ['What is Programming?', 'Basics of Programming']

p_content = [
    """<div>
    <h1>What is Programming?</h1>
    <p>Programming is the process of designing and building executable computer software to accomplish a specific task. It involves writing code in various programming languages, such as Python, Java, C++, and more.</p>
    <p>Key concepts in programming include:</p>
    <ul>
        <li><strong>Algorithms:</strong> A set of instructions to solve a problem.</li>
        <li><strong>Data Structures:</strong> Organizing and storing data efficiently.</li>
        <li><strong>Syntax:</strong> The set of rules that defines the combinations of symbols that are considered to be correctly structured programs.</li>
    </ul>
    <img src="https://example.com/what_is_programming.jpg" alt="What is Programming" style="max-width:100%;">
</div>
""",

"""<div>
    <h1>Basics of Programming Languages</h1>
    <p>Programming languages are the tools we use to write programs. They allow us to communicate with computers and give them instructions.</p>
    <h2>Types of Programming Languages</h2>
    <ul>
        <li><strong>High-Level Languages:</strong> Easier for humans to read and write (e.g., Python, Java).</li>
        <li><strong>Low-Level Languages:</strong> Closer to machine code and harder for humans to understand (e.g., Assembly).</li>
        <li><strong>Scripting Languages:</strong> Used for automating tasks (e.g., JavaScript, Bash).</li>
    </ul>
    <h2>Choosing a Language</h2>
    <p>When starting with programming, it's often recommended to choose a high-level language like Python due to its simplicity and readability.</p>
    <img src="https://example.com/programming_languages.jpg" alt="Basics of Programming Languages" style="max-width:100%;">
</div>
"""
]

for i in range(2):
    l = Lesson.objects.create(title=p_content[i], content=programming_titles[i], course=programming)
    l.save()

qs = [
    'What is Termux primarily used for?',
    'Which command would you use to change the current directory in Termux?',
    'Which command is used to install a package in Termux?',
    'To start the Python interpreter in Termux, which command would you use?',
]

ans = [1, 2, 1, 2]

choices = [
    ['To create graphical applications',
 'To provide a Linux environment on Android',
 'To play mobile games',
 'To browse the internet'],

['ls',
 'pwd',
 'cd',
 'rm'],

 ['update pkg',
 'pkg install [package-name]',
 'install pkg',
 'pkg add [package-name]'],

 ['python start',
 'run python',
 'python',
 'execute python']
]

ter_les = Lesson.objects.filter(course=termux)
for i, les in enumerate(ter_les):
    q = Quiz.objects.create(question=qs[i], answer=ans[i], lesson=les)
    q.set_options(choices[i])
    q.save()

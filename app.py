from flask import Flask, render_template, request, redirect, url_for

# Creating the app instance
app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return render_template("index.html", tasks=tasks)

# Creating a new task
@app.route('/add_task', methods=['POST'])
def create_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)  # Adding task to our list
    return redirect(url_for("home"))

# Creating a delete
@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('home'))

# Enabling the debug mode
if __name__ == "__main__":
    app.run(debug=True)

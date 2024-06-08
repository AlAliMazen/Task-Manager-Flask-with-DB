from taskmanager import db
# used to create the database model


# we use the db defined in the init file as instance of sql-Alchemy  ORM to creating the database
class Category(db.Model):
    # schema for Category model -> table
    id = db.Column(db.Integer, primary_key=True)
    # we define which column and which type of data is stored -> as string, and it should be unique, and not NULL-> enforce user to enter data
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # default function used to represent the class as string 
        return self.category_name

class Task(db.Model):
    # schema for the Task Model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # Text allows longer text
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # relation to the Category table is ONE to many , One Category to many Tasks , when category deleted, task will also be deleted.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
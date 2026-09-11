class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def test(self):
        user = {"name": "Alice", "age": 28, "city": "New York"}
        print(user, end="\n\n\n")
        ur = self.test1(user)
        print(ur, end="\n\n\n")
        print(user, end="\n\n\n")

    def test1(self, u) -> dict:
        u["lang"] = "Maithily"
        return u

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Status: {status}"


if __name__ == "__main__":
    # todo = Todo("TT", "RR")
    # todo.test()
    dctt = [{"A": 1, "B": 2}]
    for index, chart in enumerate(dctt):

        if chart.get("M"):
            print(hasattr(chart["M"], "AAAA"))
            print(hasattr(chart["M"]))
        else:
            print("No")

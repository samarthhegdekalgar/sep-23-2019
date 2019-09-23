class Employee:
    def __init__(self, first_name, last_name, employee_id, department, rate, working_hours):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department
        self.rate = rate
        self.working_hour = working_hours

    def get_fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Developer(Employee):
    def __init__(self, intensive, first_name, last_name, employee_id, department, rate, working_hour):
        self.intensive = intensive
        super(Developer, self).__init__(first_name, last_name, employee_id, department, rate, working_hour)

    def get_wages(self):
        total_wages = self.intensive + (self.working_hour * self.rate)
        return total_wages

    def get_fullname(self):
        return super(Developer, self).get_fullname()
        # return '{} {}'.format(self.first_name, self.last_name)


samarth = Developer(1000, 'Samarth', 'Hegde', 1, 'Software Designing', 10, 100)
print(samarth.get_fullname())
print(samarth.get_wages())
print(samarth.get_fullname())

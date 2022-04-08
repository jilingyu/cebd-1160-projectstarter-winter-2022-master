import DAL.db as d

dta = d.DB()

def get_all_stats():
    return dta.execute_select_query("stats")


def get_all_students():
    return dta.execute_select_query("students")


def get_provinces(_name: str):
    return dta.execute_select_query("province", params={'p': _name})

def get_lfs(_name: str):
    return dta.execute_select_query("lfs", params={'#': _name})

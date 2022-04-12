import matplotlib.pyplot as plt
from mplstyle import templates


class Style:
    def __init__(self, sty="default"):
        if sty != "default":
            stylesheet = self.get_template(sty)
            self.style = plt.style.use(stylesheet)
        else:
            self.style = plt.style.use("default")
    
    def get_template(self,template_name):
        if template_name == 'academic':
            return templates.academic
        else:
            return 'default'

    def cycle(self,cycle_name):
        pass 
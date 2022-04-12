import matplotlib.pyplot as plt
from mplstyle import templates
from mplstyle import cycles


class Style:
    def __init__(self, style_name="default"):
        '''
        style_name: name of the style to be applied
        '''
        if style_name in plt.style.available:
            self.style = plt.style.use(style_name)
        if style_name in templates.available:
            stylesheet = self.get_template(style_name)
            self.style = plt.style.use(stylesheet)
        else:
            print('Given name {} is not a valid style name. Therefore matplotlib default will be used'.format(style_name))
            self.style = plt.style.use("default")
    
    def get_template(self,template_name):
        if template_name == 'academic':
            return templates.academic
        else:
            return 'default'
    
    def cycle(self,cycle_name):
        '''
        cycle_name: name of the cycle to be cycled
        TODO: A better else clause
        '''
        if cycle_name == 'color_series':
            return cycles.color_series()
        elif cycle_name == 'linestyle_series':
            return cycles.linestyle_series()
        elif cycle_name == 'linewidth_series':
            return cycles.linewidth_series()
        elif cycle_name == 'markerstyle_series':
            return cycles.markerstyle_series()
        elif cycle_name == 'markersize_series':
            return cycles.markersize_series()
        elif cycle_name == 'linestyle_color_series':
            return cycles.linestyle_color_series()
        elif cycle_name == 'linestyle_color_marker_series':
            return cycles.linestyle_color_marker_series()
        else:
            return cycles.color_series()
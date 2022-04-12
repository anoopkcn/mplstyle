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
        if template_name in templates.available:
            attribute = getattr(templates,template_name)
            return attribute
        else:
            print('Given name |{}| is not a valid template name. Therefore matplotlib default will be used'.format(template_name))
            return 'default'
    
    def cycle(self,cycle_name):
        '''
        cycle_name: name of the cycle to be cycled
        TODO: A better else clause
        '''
        if cycle_name in cycles.available:
            method_to_call = getattr(cycles, cycle_name)
            return method_to_call()
        else:
            # Return error 
            print('Given name |{}| is not a valid cycle name. Therefore matplotlib default will be used'.format(cycle_name))
            #Reurn error 



        # if cycle_name == 'series_color':
        #     return cycles.series_color()
        # elif cycle_name == 'series_linestyle':
        #     return cycles.series_linestyle()
        # elif cycle_name == 'series_linewidth':
        #     return cycles.series_linewidth()
        # elif cycle_name == 'series_marker':
        #     return cycles.series_marker()
        # elif cycle_name == 'series_markersize':
        #     return cycles.series_markersize()
        # elif cycle_name == 'series_marker_color':
        #     return cycles.series_marker_color()
        # elif cycle_name == 'series_linestyle_color':
        #     return cycles.series_linestyle_color()
        # elif cycle_name == 'series_linestyle_marker_color':
        #     return cycles.series_linestyle_marker_color()
        # else:
        #     return cycles.series_color()
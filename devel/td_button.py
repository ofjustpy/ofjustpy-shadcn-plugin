import ofjustpy as oj
from shadcnui_components.components import Button
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *


button1 = Button(key="button1", text="Button", variant="outline", href="#", )

button2 = Button(key="button2", text="Button", variant="link", href="#", )

button3 = Button(key="button3", text="Button", variant="ghost", size="icon" )

#size="icon"
# disabled
app = oj.load_app()


tlc = oj.PD.StackV(childs=[button1, button2, button3], twtags=[space/y/4])

wp_endpoint = oj.create_endpoint(key="button",
                                 childs = [tlc
                                           ],
                                 
                                 title="Button"
                                 )
oj.add_jproute("/", wp_endpoint)
                




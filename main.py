import imgui
import glfw
import OpenGL.GL as gl
from imgui.integrations.glfw import GlfwRenderer
#from ImUi import InputStyle, FloatSliderStyle
import ImUi
from astroStyle import AstroButtonStyle, AstroInputStyle, AstroSliderStyle

def impl_glfw_init(window_name="minimal ImGui/GLFW3 example", width=1280, height=720):
    if not glfw.init():
        print("Could not initialize OpenGL context")
        exit(1)

    # OS X supports only forward-compatible core profiles from 3.2
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(int(width), int(height), window_name, None, None)
    glfw.make_context_current(window)

    if not window:
        glfw.terminate()
        print("Could not initialize Window")
        exit(1)

    return window


class GUI(object):
    def __init__(self):
        super().__init__()
        self.backgroundColor = (0, 0, 0, 1)
        self.window = impl_glfw_init()
        gl.glClearColor(*self.backgroundColor)
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)

        self.string = ""
        self.f = 0.5

        self.loop()
    

    def input_gui(self):
            imgui.new_frame()
            imgui.begin("Custom window", True)

            imgui.text("Default style")

            if ImUi.button("OK"):
                print(f"String: {self.string}")
                print(f"Float: {self.f}")

            _, self.string = ImUi.input_text("A String", self.string, 256)

            _, self.f = ImUi.slider_float("float", self.f, 0.25, 1.5)

            imgui.separator()
            # create astrostyle of the button, input_text, slider_float
            astroButtonStyle = AstroButtonStyle()
            astroInputStyle = AstroInputStyle()
            astroSliderStyle = AstroSliderStyle()   


            imgui.text("Astro style")

            if ImUi.button("OK", astroButtonStyle):
                print(f"String: {self.string}")
                print(f"Float: {self.f}")

            _, self.string = ImUi.input_text("A String", self.string, 256, astroInputStyle)

            _, self.f = ImUi.slider_float("float", self.f, 0.25, 1.5, astroSliderStyle)


            imgui.show_test_window()

            imgui.end()


    def loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            self.impl.process_inputs()
            self.input_gui()

            imgui.render()

            gl.glClearColor(*self.backgroundColor)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)

            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self.impl.shutdown()
        glfw.terminate()


if __name__ == "__main__":

    gui = GUI()
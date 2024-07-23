import glfw
from OpenGL.GL import *
import numpy as np


class App:
    def __init__(self):

        # Tratamento de erros para caso o glfw não inicie, ao mesmo tempo que chama afunção de iniciar
        if not glfw.init():
            raise Exception("GLFW não pôde ser inicializado")

        # cria uma janeça glfw e fecha o programa caso não seja possível abrir uma janela
        self.window = glfw.create_window(800, 600, "Aplicativo Minimo OpenGL", None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("A janela GLFW não pôde ser criada")

        # Definir a janela que vai usar, caso tenha mais de uma
        glfw.make_context_current(self.window)
        # Instanciar a classe triangulo
        self.poly = Polygon()
        # rodar o looping principal
        self.run()

    # Looping principal
    def run(self):
        """
        Enquanto a janela estiver aberta reconhece os eventos, faz uma limpeza de todos os píxeis da tela,
        renderiza o poligono da tela, swap_buffers eu n sei ainda.
        """
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glClear(GL_COLOR_BUFFER_BIT)
            self.poly.render()
            glfw.swap_buffers(self.window)

        """
        Fechar todos os processo da lib glfw quando terminar o looping, o looping termina quando
        o poll_events() registra o evento de fechar janela.
        """
        glfw.terminate()


class Polygon:
    def __init__(self):
        self.vertices = np.array([
            [1.0, 1.0, 0.0],
            [1.0, -1.0, 0.0],
            [-1.0, 1.0, 0.0],
            [-1.0, -1.0, 0.0]
        ], dtype=np.float32)

        self.vertex_shader_source = """
        #version 330 core
        layout (location = 0) in vec3 position;
        void main()
        {
            gl_Position = vec4(position, 1.0);
        }
        """

        self.fragment_shader_source = """
        #version 330 core
        out vec4 FragColor;
        void main()
        {
            FragColor = vec4(1.0, 1.0, 1.0, 1.0);
        }
        """

        self.VAO = None
        self.VBO = None
        self.shader_program = None

        self.init_buffers()
        self.init_shaders()

    def compile_shader(self, source, shader_type):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise RuntimeError(glGetShaderInfoLog(shader))
        return shader

    def init_shaders(self):
        vertex_shader = self.compile_shader(self.vertex_shader_source, GL_VERTEX_SHADER)
        fragment_shader = self.compile_shader(self.fragment_shader_source, GL_FRAGMENT_SHADER)

        self.shader_program = glCreateProgram()
        glAttachShader(self.shader_program, vertex_shader)
        glAttachShader(self.shader_program, fragment_shader)
        glLinkProgram(self.shader_program)
        if glGetProgramiv(self.shader_program, GL_LINK_STATUS) != GL_TRUE:
            raise RuntimeError(glGetProgramInfoLog(self.shader_program))

        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

    def init_buffers(self):
        self.VAO = glGenVertexArrays(1)
        self.VBO = glGenBuffers(1)

        glBindVertexArray(self.VAO)

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def render(self):
        glUseProgram(self.shader_program)
        glBindVertexArray(self.VAO)
        glDrawArrays(GL_POLYGON, 0, 4)
        glBindVertexArray(0)


if __name__ == "__main__":
    app = App()
from OpenGL.GL import *
import glfw
import numpy as np


def create_program(vertex_shader_file, fragment_shader_file):
    # シェーダーファイルからソースコードを読み込む
    with open(vertex_shader_file, 'r', encoding='utf-8') as f:
        vertex_shader_src = f.read()

    # 作成したシェーダオブジェクトにソースコードを渡しコンパイルする
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_src)
    glCompileShader(vertex_shader)

    with open(fragment_shader_file, 'r', encoding='utf-8') as f:
        fragment_shader_src = f.read()

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_src)
    glCompileShader(fragment_shader)

    # プログラムオブジェクト作成しアタッチ
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glDeleteShader(vertex_shader)
    glAttachShader(program, fragment_shader)
    glDeleteShader(fragment_shader)

    # 作成したプログラムオブジェクトをリンク
    glLinkProgram(program)

    return program


def create_vao():
    indices = np.array([0, 1, 2], dtype=np.uint)
    positions = np.array([[0.0, 0.5, 0.0, 1.0], [0.5, -0.5, 0.0, 1.0], [-0.5, -0.5, 0.0, 1.0]], dtype=np.float32)
    colors = np.array([[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 1.0]], dtype=np.float32)

    # 座標バッファオブジェクトを作成してデータをGPU側に送る
    position_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, position_vbo)
    glBufferData(GL_ARRAY_BUFFER, positions.nbytes, positions, GL_STATIC_DRAW)

    # 色バッファオブジェクトを作成してデータをGPU側に送る
    color_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
    glBufferData(GL_ARRAY_BUFFER, colors.nbytes, colors, GL_STATIC_DRAW)

    glBindBuffer(GL_ARRAY_BUFFER, 0)

    # VAOを作成してバインド
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # 0と1のアトリビュート変数を有効化
    glEnableVertexAttribArray(0)
    glEnableVertexAttribArray(1)

    # 座標バッファオブジェクトの位置を指定(location = 0)
    glBindBuffer(GL_ARRAY_BUFFER, position_vbo)
    glVertexAttribPointer(0, 4, GL_FLOAT, GL_FALSE, 0, None)

    # 色バッファオブジェクトの位置を指定(location = 1)
    glBindBuffer(GL_ARRAY_BUFFER, color_vbo)
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, None)

    # インデックスオブジェクトを作成してデータをGPU側に送る
    index_vbo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index_vbo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    # バッファオブジェクトとVAOをアンバインド
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao


def main():
    # GLFW初期化
    if not glfw.init():
        return

    # ウィンドウを作成
    window = glfw.create_window(640, 480, 'Hello World', None, None)
    if not window:
        glfw.terminate()
        print('Failed to create window')
        return

    # コンテキストを作成
    glfw.make_context_current(window)

    # バージョンを指定
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 0)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    program = create_program('Shader.vsh', 'Shader.fsh')
    vao = create_vao()

    while not glfw.window_should_close(window):
        # バッファを指定色で初期化
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # シェーダを有効化
        glUseProgram(program)

        glBindVertexArray(vao)

        # バインドしたVAOを用いて描画
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, None)

        glBindVertexArray(0)

        # バッファを入れ替えて画面を更新
        glfw.swap_buffers(window)

        # イベントを受け付けます
        glfw.poll_events()

    # ウィンドウを破棄してGLFWを終了
    glfw.destroy_window(window)
    glfw.terminate()


# Pythonのメイン関数はこんな感じで書きます
if __name__ == "__main__":
    main()
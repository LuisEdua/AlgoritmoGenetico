from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
import cv2 as cv
import numpy as np

def animarPlot(m, p, pr, ni):
    fig,ax = plt.subplots();
    plt.xlim(0, ni+1)
    def actualizarPlot(i):
        ax.clear()
        ax.plot(np.arange(i + 1), m[:i + 1], label="Mejores casos")
        ax.plot(np.arange(i + 1), p[:i + 1], label="Peores casos")
        ax.plot(np.arange(i + 1), pr[:i + 1], label="Casos promedio")
        plt.legend()
        plt.title("Evolución")
        plt.xlabel("Generaciones")
        plt.text(0, 15, "Aqui le entrego")
        plt.ylabel("Valor del fitness")
    animar = FuncAnimation(fig, actualizarPlot,range(len(pr)),interval=100, cache_frame_data=False, repeat = False)
    grabarAnimacion(animar)

def grabarAnimacion(animar):
    writer = FFMpegWriter(fps=4, metadata=dict(artist='Luis'), bitrate=1800)
    animar.save("Animación Evolucion.mp4", writer=writer)

def grabarVideo(figs):
    alto, ancho = 480, 640
    fps = 0.5

    salida_video = cv.VideoWriter('Evolucion de las poblaciones.mp4',
                                  cv.VideoWriter_fourcc(*'mp4v'),
                                  fps, (ancho, alto))

    for fig in figs:
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        img = np.array(canvas.renderer.buffer_rgba())

        img = cv.cvtColor(img, cv.COLOR_RGBA2BGR)

        img = cv.resize(img, (ancho, alto))

        salida_video.write(img)

    salida_video.release()

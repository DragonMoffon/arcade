from typing import NamedTuple, Optional, TYPE_CHECKING

from arcade.camera import Projector
from arcade.camera.projection_functions import generate_orthographic_matrix

from pyglet.math import Mat4

if TYPE_CHECKING:
    from arcade.context import ArcadeContext

class CameraState(NamedTuple):
    view: Mat4
    projection: Mat4
    viewport: tuple[int, int, int, int]
    scissor: Optional
    projector: Projector


class CameraStack:

    def __init__(self, context: ArcadeContext):
        self._context: ArcadeContext = context
        self._stack: list[CameraState] = []

    def push(self, camera_state: CameraState):
        self._stack.append(camera_state)

    def pop(self) -> CameraState:
        if len(self._stack) == 1:
            raise ValueError("Cannot pop final element of CameraStack")
        return self._stack.pop()

    def peek(self) -> CameraState:
        return self._stack[-1]

    def clear(self):
        self._stack.clear()
        self._context.
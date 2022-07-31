from .io.abc import FileFormatType


class OBJFileFormat(FileFormatType):
    EXTENSION = ".obj"

    VERTEX_TAG = "v"
    NORMAL_TAG = "vn"
    PARAMETER_TAG = "vp"
    FACE_TAG = "f"
    TEXTURE_TAG = "vt"
    LINE_TAG = "l"
    COMMENT_TAG = "#"
    SHADING_TAG = "s"
    LIBRARY_TAG = "mtllib"
    USE_TAG = "usemtl"

    OBJECT_TAG = "o"
    GROUP_TAG = "g"

    NULL_FACE_TEXTURE = ""
    VERTEX_SEPARATOR = "/"
    DOUBLE_VERTEX_SEPARATOR = VERTEX_SEPARATOR + VERTEX_SEPARATOR

import re


class OBJContentToken(OBJTokenComponent):
    def __init__(self, tag, *parameters, comment=""):
        self._tag = tag
        self._parameters = parameters
        self._comment = comment

    def tag(self): return self._tag
    def parameters(self): return self._parameters
    def comment(self): return self._comment

    def is_vertex(self): return self._tag == self.VERTEX_TAG
    def is_normal(self): return self._tag == self.NORMAL_TAG
    def is_texture(self): return self._tag == self.TEXTURE_TAG
    def is_parameter(self): return self._tag == self.PARAMETER_TAG
    def is_line(self): return self._tag == self.LINE_TAG
    def is_face(self): return self._tag == self.FACE_TAG
    def is_library(self): return self._tag == self.LIBRARY_TAG
    def is_object(self): return self._tag == self.OBJECT_TAG
    def is_group(self): return self._tag == self.GROUP_TAG


class OBJContentHandler(OBJTokenComponent):
    def __init__(self):
        self._vertices = []
        self._normals = []
        self._textures = []
        self._parameters = []
        self._lines = []
        self._faces = []
        self._libraries = []
        self._objects = []

    def vertices(self): return tuple(self._vertices)
    def normals(self): return tuple(self._normals)
    def textures(self): return tuple(self._textures)
    def parameters(self): return tuple(self._parameters)
    def lines(self): return tuple(self._lines)
    def faces(self): return tuple(self._faces)
    def libraries(self): return tuple(self._libraries)
    def objects(self): return tuple(self._objects)





class OBJContentBuilder(OBJContentHandler):
    def __init__(self, *args, header="", **kwargs):
        super().__init__(*args, **kwargs)
        self._header = header
        self._vertices_comment = "-" * 3 + " Vertex definitions ".ljust("-", 32)
        self._normals_comment = "-" * 3 + " Normal definitions ".ljust("-", 32)
        self._textures_comment = "-" * 3 + " Texture definitions ".ljust("-", 32)
        self._parameters_comment = "-" * 3 + " Parameter definitions ".ljust("-", 32)
        self._lines_comment = "-" * 3 + " Line definitions ".ljust("-", 32)
        self._faces_comment = "-" * 3 + " Face definitions ".ljust("-", 32)
        self._libraries_comment = "-" * 3 + " Library definitions ".ljust("-", 32)
        self._objects_comment = "-" * 3 + " Object definitions ".ljust("-", 32)

    def header(self): return self._header
    def vertices_comment(self): return self._vertices_comment
    def normals_comment(self): return self._normals_comment
    def textures_comment(self): return self._textures_comment
    def parameters_comment(self): return self._parameters_comment
    def lines_comment(self): return self._lines_comment
    def faces_comment(self): return self._faces_comment
    def libraries_comment(self): return self._libraries_comment
    def objects_comment(self): return self._objects_comment

    def set_header(self, comment): self._header = comment
    def set_vertices_comment(self, comment): self._vertices_comment = comment
    def set_normals_comment(self, comment): self._normals_comment = comment
    def set_textures_comment(self, comment): self._textures_comment = comment
    def set_parameters_comment(self, comment): self._parameters_comment = comment
    def set_lines_comment(self, comment): self._lines_comment = comment
    def set_faces_comment(self, comment): self._faces_comment = comment
    def set_libraries_comment(self, comment): self._libraries_comment = comment
    def set_objects_comment(self, comment): self._objects_comment = comment

    def from_component(self, component):
        pass

    def from_tokens(self, tokens):
        for token in tokens:
            self._vertices.append(token) if token.is_vertex() else None
            self._normals.append(token) if token.is_normal() else None
            self._textures.append(token) if token.is_texture() else None
            self._parameters.append(token) if token.is_parameter() else None
            self._lines.append(token) if token.is_line() else None
            self._faces.append(token) if token.is_face() else None
            self._libraries.append(token) if token.is_library() else None
            self._objects.append(token) if token.is_object() else None
        return self

    @staticmethod
    def render_comment(comment, indent=0, sep="\n", comment_end=None, end=""):
        return sep.join(
            " " * indent + "# " + line for line in comment.splitlines()
            ) + end if comment_end is None else comment_end

    @staticmethod
    def render_parameters(tag, parameters, indent=0, parameter_end=None, end=""):
        return " " * indent + tag() + " " \
            + " ".join(str(p) for p in parameters) \
            + end if parameter_end is None else parameter_end

    @classmethod
    def render_token(cls, token, tag_end="", **kwargs):
        return cls.render_comment(token.comment(), **kwargs) + "\n" \
            + cls.render_parameters(token.tag(), token.parameters(), **kwargs) \
            + tag_end

    @classmethod
    def render_section(cls, section, header="", section_end=None, end="", **kwargs):
        return cls.render_comment(header, end=end, **kwargs) + "\n" \
            + "\n".join(
                (cls.render_token(i, renderer, end=end, **kwargs) for i in section)
                ) + end if section_end is None else section_end

    def render_vertices(cls, **kwargs):
        return cls.render_section(self._vertices, **kwargs)
    def render_normals(cls, **kwargs):
        return cls.render_section(self._normals, **kwargs)
    def render_textures(cls, **kwargs):
        return cls.render_section(self._textures, **kwargs)
    def render_parameters(cls, **kwargs):
        return cls.render_section(self._parameters, **kwargs)
    def render_lines(cls, **kwargs):
        return cls.render_section(self._lines, **kwargs)
    def render_faces(cls, **kwargs):
        return cls.render_section(self._faces, **kwargs)
    def render_libraries(cls, **kwargs):
        return cls.render_section(self._libraries, **kwargs)
    def render_objects(cls, **kwargs):
        return cls.render_section(self._objects, **kwargs)

    def render(self, **kwargs):
        return "\n".join((
            self._render_vertices(**kwargs),
            self._render_normals(**kwargs),
            self._render_textures(**kwargs),
            self._render_parameters(**kwargs),
            self._render_lines(**kwargs),
            self._render_faces(**kwargs),
            self._render_libraries(**kwargs),
            self._render_objects(**kwargs)
            ))

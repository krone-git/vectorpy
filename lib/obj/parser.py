

class OBJContentParser(OBJContentHandler):
    TAG_SUFFIX_PATTERN = "\s+.*"

    @staticmethod
    def tag_pattern(cls, tag): return tag + cls.TAG_SUFFIX_PATTERN

    def parse_content(self, content):
        self._vertices = self.parse_content_vertices(content)
        self._normals = self.parse_content_normals(content)
        self._textures = self.parse_content_textures(content)
        self._parameters = self.parse_content_parameters(content)
        self._lines = self.parse_content_lines(content)
        self._faces = self.parse_content_faces(content)
        self._libraries = self.parse_content_libraries(content)
        self._objects = self.parse_content_objects(content)

    @classmethod
    def parse_numeric_content(cls, tag, content, pattern, type):
        return [
            OBJContentToken(
                tag, *cls.parse_numeric_parameters(line, pattern, type)
                )
            for line in re.findall(cls.tag_pattern(tag), content)
            ]

    @staticmethod
    def parse_numeric_parameters(line, pattern, type):
        return [type(p.group(0)) for p in re.finditer(pattern, line)]

    @classmethod
    def parse_content_vertices(cls, content):
        return cls.parse_numeric_content(
            cls.VERTEX_TAG, content, cls.RE_NUMBER_PATTERN, float
            )

    @classmethod
    def parse_content_normals(cls, content):
        return cls.parse_numeric_content(
            cls.NORMAL_TAG, content, cls.RE_NUMBER_PATTERN, float
            )

    @classmethod
    def parse_content_textures(cls, content):
        return cls.parse_numeric_content(
            cls.TEXTURE_TAG, content, cls.RE_NUMBER_PATTERN, float
            )

    @classmethod
    def parse_content_parameters(cls, content):
        return cls.parse_numeric_content(
            cls.PARAMETER_TAG, content, cls.RE_NUMBER_PATTERN, float
            )

    @classmethod
    def parse_content_line(cls, content):
        return cls.parse_numeric_content(
            cls.LINE_TAG, content, cls.RE_INTEGER_PATTERN, int
            )

    @classmethod
    def parse_content_faces(cls, content):
        pattern = cls.tag_pattern(cls.FACE_TAG)
        return [cls.parse_face(face) for face in re.findall(pattern, content)]

    @classmethod
    def parse_content_libraries(cls, content): return []
    @classmethod
    def parse_content_objects(cls, content): return []

    @classmethod
    def parse_vector(cls, line):
        return cls.parse_numerical_parameters(line, cls.RE_NUMBER_PATTERN, float)
    @classmethod
    def parse_normal(cls, line):
        return cls.parse_numerical_parameters(line, cls.RE_NUMBER_PATTERN, float)
    @classmethod
    def parse_texture(cls, line):
        return cls.parse_numerical_parameters(line, cls.RE_NUMBER_PATTERN, float)
    @classmethod
    def parse_line(cls, line):
        return cls.parse_numerical_parameters(line, cls.RE_INTEGER_PATTERN, int)

    @classmethod
    def parse_face(cls, line):
        face = []
        for vertex in line.split()[1:]:
            parameters = [
                int(p) for p in re.findall(cls.RE_INTEGER_PATTERN, vertex)
                ]
            if cls.DOUBLE_VERTEX_SEPARATOR in face:
                parameters.insert(1, None)
        return face

    @classmethod
    def parse_face_parameter(cls, parameter):
        pass

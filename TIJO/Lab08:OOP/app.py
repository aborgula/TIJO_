from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class Figure:
    def __init__(self, name, color="#808080"):
        self.name = name
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def to_dict(self):
        return {self.name: self.color}
    
class Square(Figure):
    def __init__(self, color="#808080"):
        super().__init__("square", color)

class Circle(Figure):
    def __init__(self, color="#808080"):
        super().__init__("circle", color)

class Triangle(Figure):
    def __init__(self, color="#808080"):
        super().__init__("triangle", color)

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def change_color(self, figure_type, new_color):
        figure = self.figures.get(figure_type)
        if figure:
            figure.change_color(new_color)
            return True
        return False
    
    def change_color_all(self, new_color):
        for fig in self.figures.values():
            fig.change_color(new_color)

    def get_colors(self):
        return {name: fig.color for name, fig in self.figures.items()}
    

figure_service = FigureService()


@app.route('/')
def index():
    return render_template('index.html', figure_colors=figure_colors)


@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if figure_service.change_color(figure_type, new_color):
        return jsonify({"status": "success", "figure_colors": figure_service.get_colors()})
    return jsonify({"status": "error", "message": "figure type error"}), 400


@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')

    if new_color:
        figure_service.change_color_all(new_color)
        return jsonify({"status": "success", "figure_colors": figure_colors})
    return jsonify({"status": "error", "message": "new color error"}), 400

if __name__ == '__main__':
    app.run(debug=True)
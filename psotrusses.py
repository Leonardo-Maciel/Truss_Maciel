class Createtruss:

    def __init__(self, x, y, connect):
        self.x = x
        self.y = y
        self.connect = connect
        self.point = []
        self.x1 = []
        self.y1 = []

    def plot(self, plot='no'):
        if plot == 'yes':
            for xi, yi in zip(self.x, self.y):
                self.point.append([xi, yi])
                plt.scatter(xi, yi, color='grey')
            for i in range(len(self.connect)):
                self.x1.append(self.point[self.connect[i][0]][0])
                self.x1.append(self.point[self.connect[i][1]][0])
                self.y1.append(self.point[self.connect[i][0]][1])
                self.y1.append(self.point[self.connect[i][1]][1])
            plt.plot(self.x1, self.y1)
            plt.show()

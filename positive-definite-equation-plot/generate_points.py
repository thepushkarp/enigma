"""Generates w, x, y, z and f(w, x, y, z) and saves them to csv files"""
import os

def generate_points():
    for i in range(-10, 10 + 1):
        # Create a folder for each value of w
        print(f'Generating files for w = {i}')
        dirname = os.path.join('csvs', 'csv{:0>2d}'.format(i + 10))
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        for j in range(-10, 10 + 1):
            # Create a file for each value of x
            filename = os.path.join(dirname, 'file{:0>2d}.csv'.format(j + 10))
            file = open(filename, 'w+')
            for k in range(-10, 10 + 1):
                for l in range(-10, 10 + 1):
                    f = i*i + 2*j*j + 2*k*k + 11*l*l + 2*i*k + 4*i*l - 4*j*l
                    file.write(f"{i},{j},{k},{l},{f}\n")
            file.close()

if __name__ == "__main__":
    generate_points()

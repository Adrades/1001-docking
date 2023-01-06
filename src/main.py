from biopandas.pdb import *
from pandas import DataFrame
from sys import argv

"""
Cli for splitting pdb in 27 groups
"""

def struct_init(columns)-> list:
    return [
        # DataFrame(columns=columns)
        list()
        for _ in range(27)
    ]

def main():
    file = PandasPdb().read_pdb(argv[1])
    xmax, ymax, zmax = file.df["ATOM"][["x_coord", "y_coord", "z_coord"]].max()
    xmin, ymin, zmin = file.df["ATOM"][["x_coord", "y_coord", "z_coord"]].min()

    df = struct_init(list(file.df["ATOM"].columns))

    s1_1 = .30
    s1_2 = .36
    s2_1 = .63
    s2_2 = .69

    for index, row in file.df["ATOM"].iterrows():
        x, y, z = row[["x_coord", "y_coord", "z_coord"]]
        if x <= xmin + s1_2 * (xmax-xmin) :
            if y <= ymin + s1_2 * (ymax-ymin) :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[0].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[1].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[2].append(row)
            if ymin + s1_1 * (ymax-ymin) <= y <= ymin + s2_2 * (ymax-ymin):
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[3].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[4].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[5].append(row)
            if ymin + s2_1 * (ymax-ymin) <= y :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[6].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[7].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[8].append(row)
        if xmin + s1_1 * (xmax-xmin) <= x <= xmin + s2_2 * (xmax-xmin):
            if y <= ymin + s1_2 * (ymax-ymin) :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[9].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[10].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[11].append(row)
            if ymin + s1_1 * (ymax-ymin) <= y <= ymin + s2_2 * (ymax-ymin):
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[12].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[13].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[14].append(row)
            if ymin + s2_1 * (ymax-ymin) <= y :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[15].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[16].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[17].append(row)
        if xmin + s2_1 * (xmax-xmin) <= x:
            if y <= ymin + s1_2 * (ymax-ymin) :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[18].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[19].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[20].append(row)
            if ymin + s1_1 * (ymax-ymin) <= y <= ymin + s2_2 * (ymax-ymin):
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[21].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[22].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[23].append(row)
            if ymin + s2_1 * (ymax-ymin) <= y :
                if z <= zmin + s1_2 * (zmax-zmin):
                    df[24].append(row)
                if zmin + s1_1 * (zmax-zmin) <= z <= zmin + s2_2 * (zmax-zmin):
                    df[25].append(row)
                if zmin + s2_1 * (zmax-zmin) <= z:
                    df[26].append(row)

    for i in range(27):
        df[i] = DataFrame(data=df[i], columns=file.df["ATOM"].columns)
        # print(df[i].head)

if __name__ == "__main__":
    main()

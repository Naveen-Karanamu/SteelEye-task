                
import csv
import xml.etree.ElementTree as ET

# file_path="D:\Local disk(E)\SteelEye\DLTINS_20210117_01of01.xml"
# csv_name="data.csv"

def xml_to_csv(file_path, csv_name) -> None:
    tree=ET.parse(file_path)
    root=tree.getroot()
    print(root)
    
    with open(csv_name,"m")as csv_file:
        writer = csv.writer(csv_file)
        headers=(child.tag for child in root[8])
        writer.writerow(headers)
        num_records=len(root)
        
        for record in range(num_records):
            rec=(child.text for child in root[record])
            writer.writerow(rec)
            
if __name__=='__main__':
    import sys
    import pathlib
    
    try:
        file_path = sys.argv[1]
        csv_name=sys.argv[2]
        
    except IndexError:
        sys.exit("Two arguments requied. One xml path and one savee file name.")
        
        with pathlib.Path(file_path) as xml_file:
            if xml_file.is_file():
                xml_to_csv(file_path, csv_name)
                
            else:
                sys.exit("Did not find {file_path}")
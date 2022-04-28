# Stand: 22.04.21
# Beispiel für Dateifunktionen
# und Exceptions

import simple as sf
import jsonfile as jf
import json

def main():
    # Fehler können getestet werden, wenn der Dateiname geändert ist
    try:
        value, value1 = sf.read_my_file("simplefile.txt")
    except Exception as e:
         print(e)
    finally: 
        # wird immer aufgerufen am Ende des Try/Expept Blocks
        # aufgerufen, auch wenn kein Fehler vorliegt
        print("Ich werde immer als letztes angezeigt")

    print(value, value1)
    print(sf.read_my_file1("simplefile.txt"))
    #sf.write_my_file("simplefile.txt", random.randint(0, 9999))

    ## JSON example
    jso = jf.read_my_jsonfile("jsonfile.json")
    print(jso)
    
    jso[0]['name'] = "Peter"
    print(jso)

    jf.write_my_file("jsonfile1.json", json.dumps(jso, indent=2))

if __name__ == "__main__":
    main()
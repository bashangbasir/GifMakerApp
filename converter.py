import imageio
import os


class Converter:      

    def convertToTargetFormat(self, inputPath, targetFormat):
        outputPath = os.path.splitext(inputPath)[0] + targetFormat
        
        reader = imageio.get_reader(inputPath)
        fps = 10    
        
        writer = imageio.get_writer(outputPath,fps=fps)
        for frames in reader:
            writer.append_data(frames)
            
        writer.close()
        reader.close()
    
    def getFps(self, inputPath):
        reader = imageio.get_reader(inputPath)
        fps = reader.get_meta_data()["fps"]
        reader.close()
        return fps

    def getDuration(self, inputPath):
        reader = imageio.get_reader(inputPath)
        duration = reader.get_meta_data()["duration"]
        reader.close()
        return duration

    def getSizeXY(self, inputPath):
        reader = imageio.get_reader(inputPath)
        size = reader.get_meta_data()["size"]
        x_size, y_size = size[0],size[1]
        reader.close()
        return x_size, y_size

'''
def main():
    cv = Converter()
    clip = os.path.abspath("1.mp4")
    fps = cv.getFps(clip)
    x_size,y_size = cv.getSizeXY(clip)
    duration = cv.getDuration(clip)
    cv.converterMaker(clip,".gif")

if __name__ == "__main__":
    main()
 '''

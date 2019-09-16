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
    
    def getMetadata(self,inputPath):
        reader = imageio.get_reader(inputPath)
        metadata = reader.get_meta_data()
        return metadata

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

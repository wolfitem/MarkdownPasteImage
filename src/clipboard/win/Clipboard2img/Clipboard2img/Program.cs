using System;
using System.IO;
using System.Linq;
using System.Windows;
using System.Windows.Media.Imaging;

namespace Clipboard2img
{
    internal class Program
    {
        [STAThread]
        private static void Main(string[] args)
        {
            string Path = "c:\\aaa.jpg";
            if (args.Count<string>() > 0)
            {
                Path = args[0];
            }
            string result = Program.SaveClipboardImage(Path);
            Console.Out.WriteLine(result);
        }
        public static string SaveClipboardImage(string storingPath)
        {
            string result = "剪切板中没有图片";
            try
            {
                BitmapSource image = Clipboard.GetImage();
                if (image != null)
                {
                    result = storingPath.Trim();
                    FileStream stream = File.Open(result, FileMode.CreateNew);
                    new JpegBitmapEncoder
                    {
                        QualityLevel = 80,
                        Frames =
                        {
                            BitmapFrame.Create(image)
                        }
                    }.Save(stream);
                    stream.Dispose();
                }
            }
            catch (Exception e)
            {
                result = "也许你动作太快了";
                result += e.Message;
            }
            return result;
        }
    }
}

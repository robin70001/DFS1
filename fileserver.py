import web
import mywebclass

urls = (
  '/(.*)', 'index'
)

url1 = "./srvfile/file1_b.txt"

class index:
    def GET(self, filename):
      print(filename)
      with open(filename) as file1:
        text1 = file1.read()
      return text1
    
    def POST(self, filename):
      with open(filename,'w') as wfile:
        content = web.data().decode()
        wfile.write(content)
        
      with open(url1,'w') as wfile:
        wfile.write(content)
        
        return "Write Success"
      
    
    

if __name__ == "__main__":
    #app = web.application(urls, globals())
    app = mywebclass.mywebclass(urls, globals())
    app.run(port = 8081)
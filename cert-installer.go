import (
	"fmt"
	"os"
	"os/exec"
	"io/ioutil"
	"time"
)

func main() {
	pwd, err := os.Getwd()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println(pwd)
	fmt.Println(pwd+"\\myCA.cer")
	certaddcmd := []byte(`certutil -f -addstore "Root" %1
pause`)
	_ = ioutil.WriteFile(pwd+"\\run.cmd", certaddcmd, 777)
	c, _ := exec.Command("run.cmd", pwd+"\\myCA.cer" ).Output()
	fmt.Print(string(c))
	time.Sleep(10000 * time.Millisecond)
}


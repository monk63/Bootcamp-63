using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace HelloWorld.TestTools
{
    //Test class attribute
    [TestClass]
    public class WhenProgramRuns
    {
        private string _consoleOutput;

        [TestInitialize]
        public void TestInitialize()
        {
            var w = new System.IO.StringWriter();
            Console.SetOut(w);

            Program.Main(new string[0]);

            _consoleOutput =w.GetStringBuilder().ToString().Trim();
        }
        [TestMethod]
        public void sayHelloWorld(){
            Assert.AreEqual("Hello, world!", _consoleOutput);
        }

    }
}

from cppyy import cppdef

cppdef("""
std::string hello() {
   std::string s = "Hello Qt World Summit 2019!";
   return s;
}
""")

if __name__ == "__main__":
    from cppyy.gbl import hello
    print(hello())

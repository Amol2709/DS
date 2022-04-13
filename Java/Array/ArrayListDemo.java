import java.util.ArrayList;


class Student{
	private String name;
	private int age;
	Student(String name,int age){
		this.name= name;
		this.age = age;
	}

	public void printData(){
		System.out.println(name+" "+age);
	}
}



class ArrayListDemo{
	public static void main(String[] args){
		ArrayList <Student> obj = new ArrayList <Student>(3);
		Student S1 = new Student("Amol",25);
		obj.add(S1);
		obj.add(new Student("Chintu",24));
		obj.add(new Student("Chintu2",26));
		obj.add(S1);
		obj.add(new Student("Chintu3",28));
		obj.forEach(p -> p.printData());
	}
}
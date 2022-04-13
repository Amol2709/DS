class Student<T extends Number>{
	String name;
	T [] marks;

	Student(T [] m){
		marks = m;
	}

	double Total(){
		double sum=0.0;
		for (int i = 0;i<marks.length;i++){
			sum = sum+marks[i].doubleValue();
		}
		return (sum);
	}

	void demo(Student<T> OBJ){
		double ans = Total()+OBJ.Total();
		System.out.println("Ans: "+ ans);
	}
}



class GenDemo{
	public static void Sum(){
		System.out.println("Amol");
	}
	public static void main(String[] args){
		Integer intmarks[] = {10,20,30};
		Student<Integer> obj = new Student<Integer>(intmarks);
		System.out.println("Ans1: "+ obj.Total());
		
		Sum();

		Integer intmarks2[] = {10,20,30};
		Student<Integer> obj2 = new Student<Integer>(intmarks2);
		System.out.println("Ans1: "+ obj2.Total());


		obj.demo(obj2);
	}
}
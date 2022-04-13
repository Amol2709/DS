
//***************** Generic Method **************************************

class Demo{
	public <T> void genM(T t){
		System.out.println(t);
	}


	public static void main(String [] args){
		Demo obj = new Demo();
		obj.genM(100);
		obj.genM(100.214);
		obj.genM("Amol");
	}
}



// ******************** Generic Class ***********************************
// class Sample <E> {
// 	E e;
// 	public Sample(E e){
// 		this.e =e;
// 	}
// 	public void setE(E e){
// 		this.e =e;
// 	}
// 	public E getE(){
// 		return e;
// 	}
// }

// class Demo{
// 	public static void main(String [] args){
// 		Sample <String> obj = new Sample <String> ("amol");
// 		Sample <Integer> obj2 = new Sample <Integer> (200);
// 		System.out.println(obj.getE());
// 		System.out.println(obj2.getE());
// 	}
// }




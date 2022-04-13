// class SwapTest{
// 	public <T> void genSwap(T x,T y){
// 		T temp;
// 		temp = x;
// 		x=y;
// 		y=temp;
// 	}

// 	public static void main(String [] args){
// 		SwapTest obj = new SwapTest();
// 		obj.genSwap(30,40);
// 	}
// }


class Test <T>{
	T x;
	T y;
	Test (T x, T y){
		this.x = x;
		this.y = y;
	}
	public T[] swap(){
		// T temp;
		// temp = x;
		// x=y;
		// y=temp;

		T[] ans = new T [2]; 
		ans[0]=y;
		ans[1]=x;
		return ans;
	}

}


class SwapTest{
	public static void main(String[] args){
		Test <Integer> obj = new Test <Integer>(30,49);
		obj.swap();
	}
}
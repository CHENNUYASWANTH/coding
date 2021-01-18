class Solution {
   public  void visit(int[][] image,int or,int sr,int sc,int newcolor,int r,int c){
       if(sr<0 || sr>=r || sc<0 || sc>=c || image[sr][sc]!=or)
           return;
       image[sr][sc]=newcolor;
       visit(image,or,sr+1,sc,newcolor,r,c);     
visit(image,or,sr,sc+1,newcolor,r,c); 
visit(image,or,sr-1,sc,newcolor,r,c);
visit(image,or,sr,sc-1,newcolor,r,c);
   }
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if(newColor==image[sr][sc])
            return image;
        int r=image.length;
        int c=image[0].length;
        int or=image[sr][sc];
        visit(image,or,sr,sc,newColor,r,c);

        
      return image;  
    }
}
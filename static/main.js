var view = document.getElementById("view"); //获取canvas元素标签
var WIDTH="700";
var HEIGHT="700";
var cards = [];
view.width=WIDTH;							//传递宽高给canvas
view.height=HEIGHT;
var faceUpNum=0;
var lastClick=0;
var fakeId=[];								//生成fakeid
var flipCount =0;
for(var i=0;i<16;i++)						//产生随机数
	{
		fakeId[i]=parseInt(i/2);
	}
for(var i=0;i<16;i++)
	{
		var swap = fakeId[i];
		var rad = parseInt(Math.random()*16);
		fakeId[i]=fakeId[rad];
		fakeId[rad]=swap;

	}
var ctx=view.getContext("2d");				//生成用于在画布上绘图的环境
function createBackground(){				//创建背景
ctx.fillStyle="rgba(110,110,110,1)";
ctx.fillRect(0,0,600,600);
}
createBackground();
var cardObj = function(i){
	var row = parseInt(i/4);
	var col = i%4;
	this.id=i;
	this.isFacedUp=false;
	this.isMatched=false;
	this.width=WIDTH/5;
	this.height="150";
	this.leftX=col*(WIDTH/5+10)+5;
	this.leftY=row*(HEIGHT/5+10)+5;
	this.rightX=WIDTH/5;
	this.rightY=(HEIGHT/5);
	this.fakeId = fakeId[i];
};
cardObj.prototype.click = function(){
	alert("123");
};

for(var i=0;i<16;i++)
	{
		cards[i]=new cardObj(i);
		drawCard(i);
	}
function drawCard(i){						//绘制卡片

	if (cards[i].isFacedUp==false){
		ctx.fillStyle="rgba(20,158,194,1)";
		ctx.fillRect(cards[i].leftX,cards[i].leftY,cards[i].rightX,cards[i].rightY);

	}
	else{
		ctx.fillStyle="rgba(158,158,194,1)";
		ctx.fillRect(cards[i].leftX,cards[i].leftY,cards[i].rightX,cards[i].rightY);
		ctx.font = '40px Adobe Ming Std';
		ctx.fillStyle="rgba(0,0,0,1)";
        ctx.fillText(cards[i].fakeId,cards[i].leftX+cards[i].width/2-10,cards[i].leftY+cards[i].height/2);
	}
	if(cards[i].isMatched==true){
		ctx.fillStyle="rgba(110,110,110,1)";
		ctx.fillRect(cards[i].leftX,cards[i].leftY,cards[i].rightX,cards[i].rightY);
	}

	//console.log(cards[i]);
}
function drawCount(i){				//绘制次数
		ctx.fillStyle="#fff";
		ctx.fillRect(210,610,200,200);
		ctx.font = '40px Adobe Ming Std';
		ctx.fillStyle="rgba(0,0,0,1)";
        ctx.fillText(i,250,650);
}
function update(i){
	drawCount(flipCount++);
	for(var k=0;k<16;k++)
	{
		drawCard(k);
	}
				faceUpNum+=1;
	if(faceUpNum==2){
		if(lastClick==i)
			{
				faceUpNum-=1;

			}
		else{
			if(cards[lastClick].fakeId==cards[i].fakeId&&lastClick!=i){
			cards[lastClick].isMatched=true;
			cards[i].isMatched=true;
		}
		else{
		cards[i].isFacedUp=false;
		cards[lastClick].isFacedUp=false;
		}
		faceUpNum=0;
		}

	}

		lastClick=i;

}
function cardClick(e){    //点击事件
	var x=e.offsetX;
	var y=e.offsetY;
	console.log("x:"+x+" y:"+y);

	for(var i=0;i<16;i++)
	{
		if(x>cards[i].leftX&&x<cards[i].leftX+cards[i].rightX&&y>cards[i].leftY&&y<cards[i].rightY+cards[i].leftY){
			if(cards[i].isFacedUp==true){

			}
			else{
			cards[i].isFacedUp=true;

			update(i);
			}


		}
	}
}
view.addEventListener("click",cardClick,false);

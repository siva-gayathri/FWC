module main(
	input P,Q,R,S;
output H;
);
assign H = (!(Q&&S)) || ((!P)&&S) || (P&&Q&&R) || (P&&(!Q)&&(!    R)&&S);                                                   endmodule

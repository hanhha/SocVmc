soc = {
	"name" : "UART",
	"filename" : "UART.sv",
	"libs" : ["../Common", "../QIf"],
	"desc" : [
		"HMTH (c)",
		"Simple handshake protocol to UART",
					 ],
	"ios" : {
						"tx_irq":{"type": "output", "width" : 1},
						"rx_irq":{"type": "output", "width" : 1},
					},
	"codes" : [
							"assign tx_irq = 1'b0;",
							"assign rx_irq = 1'b0;",
						],
	"subblocks" :	{
										"QIf": {"filename" : "QIf.sv", "instance" : "QIf",
														"params"  : { "DW" : 8, "TX_DEPTH" : 8, "RX_DEPTH" : 8},
														"inputs"  : {
																	"req_wait : 1'b1",
																	"txq_re   : tx_gnt",
																	"rxq_we   : rx_vld",
																	"rxq_dat  : rx_dat",
														 	  },
														"outputs" : {
																	"rsp_err" : "", # Don't use this signal for now
																	"txq_empty_n" : "tx_vld",
																	"txq_dat"     : "tx_dat",
																	"rxq_full_n"  : "rx_gnt",        # Don't use this signal for now
																},
													 },
										"UART_TX": {"filename" : "UART_TX.sv", "instance" : "UART_TX",
										            "params"  : { "CLK_PER_BAUD" : "CLK_PER_BAUD", "TW" : "TW"},
										            "inputs"  : {
										            							"vld" :"tx_vld",
										            							"dat" :"tx_dat",
										            				 	  },
										            "outputs" : {
										            							"gnt" : "tx_gnt",
										            						},
									             },
										"UART_RX": {"filename" : "UART_RX.sv", "instance" : "UART_RX",
										            "params"  : { "CLK_PER_BAUD" : "CLK_PER_BAUD", "TW" : "TW"},
										            "inputs"  : {
										            							"gnt" : "rx_gnt",
										            				 	  },
										            "outputs" : {
										            							"vld" : "rx_vld",
										            							"dat" : "rx_dat",
										            						},
									             },
								 }
}

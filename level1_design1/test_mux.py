# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')
    var = [inp0, inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8, inp9, inp10, inp11, inp12, inp13, inp14, inp15, inp16, inp17, inp18, inp19, inp20,inp21, inp22, inp23, inp24, inp25, inp26, inp27, inp28, inp29] = [i for i in range(30)]

    num = 0
    for i in var:
        dut.var[i] = num
        num+=1
    count = 0
    while count < 29:
        print ("Selectline",count)
        dut.sel = bin(count)
        assert dut.out == var[i], f"MUX result is incorrect: {dut.out.value} != {count}"
        count+=1

    
    





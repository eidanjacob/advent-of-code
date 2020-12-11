import pdb;
ops = open("input.txt").readlines()
wire_values = dict()
ops_not_run = []

def part1(ops):
    while len(ops) > 0:
        ops_not_run = []
        for op_unsplit in ops:
            op = op_unsplit.split(" ")
            output = op[-1].replace("\n", "")
            if any([x in op for x in ["AND", "OR", "LSHIFT", "RSHIFT"]]):
                inputs = [op[0], op[2]]
                if inputs[0] in wire_values.keys():
                    inputs[0] = wire_values[inputs[0]]
                elif inputs[0].isnumeric():
                    inputs[0] = int(inputs[0])
                else:
                    ops_not_run.append(op_unsplit)
                    continue
                if inputs[1] in wire_values.keys():
                    inputs[1] = wire_values[inputs[1]]
                elif inputs[1].isnumeric():
                    inputs[1] = int(inputs[1])
                else:
                    ops_not_run.append(op_unsplit)
                    continue
                if "AND" in op:
                    wire_values[output] = inputs[0] & inputs[1]
                elif "OR" in op:
                    wire_values[output] = inputs[0] | inputs[1]
                elif "LSHIFT" in op:
                    wire_values[output] = inputs[0] << inputs[1]
                elif "RSHIFT" in op:
                    wire_values[output] = inputs[0] >> inputs[1]
            elif "NOT" in op:
                input_signal = op[1]
                if input_signal in wire_values.keys():
                    input_signal = wire_values[input_signal]
                elif input_signal.isnumeric():
                    input_signal = int(input_signal)
                else:
                    ops_not_run.append(op_unsplit)
                    continue
                wire_values[output] = ~ input_signal
            else:
                if op[0] in wire_values.keys():
                    wire_values[output] = wire_values[op[0]]
                elif op[0].isnumeric(): 
                    wire_values[output] = int(op[0]) if output not in wire_values.keys() else wire_values[output]
                else:
                    ops_not_run.append(op_unsplit)
                    continue
        ops = ops_not_run
        
part1(ops)
a_value = wire_values["a"]
print(a_value)

wire_values = dict()
wire_values["b"] = a_value
part1(ops)
print(wire_values["a"])

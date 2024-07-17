import tkintercreator.example as b

import os

def create_script(condition_1, condition_2, output_directory):
    # Select the appropriate code block based on the first condition
    if condition_1 == 1:
        conditional_code_1 = b.conditional_code_block_1
    elif condition_1 == 2:
        conditional_code_1 = b.conditional_code_block_2
    else:
        conditional_code_1 = b.default_code_block

    # Select the appropriate code block based on the second condition
    if condition_2 == 1:
        conditional_code_2 = b.conditional_code_block_1
    elif condition_2 == 2:
        conditional_code_2 = b.conditional_code_block_2
    else:
        conditional_code_2 = b.default_code_block

    # Fill in the template with the selected code blocks
    script_content = b.base_template.format(
        conditional_code_1=conditional_code_1,
        conditional_code_2=conditional_code_2
    )

    # Define the output file path
    output_path = os.path.join(output_directory, "generated_script.py")

    # Write the generated script to a file
    with open(output_path, "w") as file:
        file.write(script_content)

    print(f"Script {output_path} created successfully.")

# Example usage
create_script(3, 2, ".")


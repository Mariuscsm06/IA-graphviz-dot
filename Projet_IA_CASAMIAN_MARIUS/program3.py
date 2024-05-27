import subprocess
import sys
import graphviz

def execute_solver(solver_path, file_path, problem_type):
    try:
        # Définition de la commande d'exécution
        command = f"java -cp {solver_path} StateGraph -n {7 if problem_type == 2 else 8} -print 1 -crossingRiver {'false' if problem_type == 2 else 'true'} -file {file_path}"

        # Exécution de la commande et capture de la sortie
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        output = result.stdout

        # Extraction des solutions
        solutions = extract_solutions(output, problem_type)
        return solutions
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande: {e}")
        print("Sortie d'erreur :")
        print(e.stderr)
        return []

def extract_solutions(output, problem_type):
    solutions = []
    collect_data = False
    
    # Recherche de la section contenant les solutions
    for line in output.splitlines():
        if "Number of Solutions" in line:
            collect_data = True
        elif collect_data and line.strip().startswith("("):
            # Extraction des solutions en fonction du type de problème
            if problem_type == 1:
                solution = extract_lcsb_solution(line)
            elif problem_type == 2:
                solution = extract_buckets_solution(line)
            solutions.append(solution)
            print("Solution extraite :", solution)  # Ajout du print pour vérification
    
    return solutions

def extract_lcsb_solution(line):
    # Extraction et traitement d'une solution pour le problème LCSB
    parts = line.strip().split(')(')
    solution = []
    for part in parts:
        part = part.replace('(', '').replace(')', '')
        left_part, right_part = part.split('|')
        state = [1 if letter in left_part else 0 for letter in 'LCSB']
        solution.append(state)
    return solution

def extract_buckets_solution(line):
    # Extraction et traitement d'une solution pour le problème des seaux
    parts = line.strip().replace("(", "").replace(")", "").split(')(')
    solution = []
    for part in parts:
        state = []
        for elem in part.split():
            if "=" in elem:
                _, value = elem.split("=")
                state.append(int(value))
        solution.append(state)
    return solution

def main():
    if len(sys.argv) != 4:
        print("Usage: python program.py <solver_path> <file_path> <problem_type>")
        sys.exit(1)

    solver_path, file_path, problem_type = sys.argv[1:]

    # Conversion du type de problème en entier
    try:
        problem_type = int(problem_type)
    except ValueError:
        print("Le type de problème doit être un entier (1 ou 2).")
        sys.exit(1)

    # Exécution du solver et extraction des solutions
    solutions = execute_solver(solver_path, file_path, problem_type)
    print(solutions)

    # essayer de trouver dans le graph.dot les solutions trouvés et mettre en gras le chemin (noeud et transitions)

if __name__ == "__main__":
    main()

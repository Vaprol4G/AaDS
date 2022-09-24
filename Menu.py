import MakeFileTask
import HashTask
import GraphTraversalTask
import GraphConstructionTask
import os

def menu():


    print("'help' для вывода всех команд")
    while (True):

        print("\nВведите команду >", end=" ")
        comand_list = {
            "help, Help - " : "Показать все команды",
            "end, End, Exit, exit - " : "Завершение программы",
            "MakeFile, MF, all - ": "Запустить задание на MakeFile",
            "MakeFileGen, gen - ": "Запустить генерацию данных из задания на MakeFile",
            "MakeFilePlot, plot - ": "Построить график из задания на MakeFile",
            "hash, Hash - ": "Запустить задание на hash",
            "GraphTraversal, GT - ": "Запустить задание на функуию обхода графа",
            "GraphConstruction, GC - ": "Запустить задание на построение графа"
        }
        def fun_help():

            print()
            for key, value in comand_list.items():
                print(key, value)

        c_input = ""
        c_input = input()
        os.system('cls||clear')
        if c_input == "help":
            fun_help()
        elif c_input == "end" or c_input == "End" or c_input == "exit" or c_input == "Exit":
            break
        elif c_input == "MakeFile" or c_input == "MF" or c_input == "all":
            MakeFileTask.mft()
        elif c_input == "MakeFileGen" or c_input == "gen":
            MakeFileTask.GFun()
        elif c_input == "MakeFilePlot" or c_input == "plot":
            MakeFileTask.PFun()
        elif c_input == "Hash" or c_input == "hash":
            HashTask.ht()
        elif c_input == "GraphTraversal" or c_input == "GT":
            GraphTraversalTask.gtt()
        elif c_input == "GraphConstruction" or c_input == "GC":
            GraphConstructionTask.gct()
        else:
            print("Неизвестная команда. Напишите help для просмотра всех команд")
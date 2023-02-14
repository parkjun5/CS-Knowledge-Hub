package jpabook.jpashop.anno;

import org.apache.commons.lang3.StringUtils;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;

// solve to
// a) define annotation @Command
// b) write function RunCommand.printCommands(), RunCommand.doCommand()
// java reflection

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@interface Command {

    String value();
    
}

class SomeObject {
    @Command("say")
    void doSay(String word) {
        System.out.println("say " + word);
    }

    @Command("tell")
    void doTell(String word) {
        System.out.println("tell " + word);
    }

    @Command("think")
    void thinkAbout(String word) {
        System.out.println("think about " + word);
    }
}

public class RunCommand {

    static void printCommands(SomeObject o) {
        Arrays.stream(o.getClass().getDeclaredMethods())
                .filter(RunCommand::hasCommandAnnotation)
                .forEach(RunCommand::printMethodByCommandAnnotation);
    }

    static void doCommand(SomeObject o, String methodName, String value) {
        Arrays.stream(o.getClass().getDeclaredMethods())
                .filter(RunCommand::hasCommandAnnotation)
                .filter(method -> StringUtils.equals(methodName, method.getAnnotation(Command.class).value()))
                .findAny().ifPresent(method -> invokeMethod(method, o, value));
    }

     static void main(String args[]){
        SomeObject o = new SomeObject();

        printCommands(o);
        // print out below example
        // say => doSay
        // tell => doTell
        // think => thinkAbout

        doCommand(o, "say", "hello");
        // say hello
        doCommand(o, "think", "world");
        // think about world
    }

    static boolean hasCommandAnnotation(Method method) {
        return method.getAnnotation(Command.class) != null;
    }

    static void printMethodByCommandAnnotation(Method method) {
        System.out.printf("%s => %s\n", method.getAnnotation(Command.class).value(), method.getName());
    }

    static void invokeMethod(Method method, Object target, String value) {
        try {
            method.invoke(target, value);
        } catch (InvocationTargetException | IllegalAccessException e) {
            System.out.println("실행 중 에러 발생" + e);
        }
    }

}